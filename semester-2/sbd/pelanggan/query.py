from db import db, get_cursor


def fetch_customer_by_id(customer_id):
    cursor = get_cursor()
    query = "SELECT id, nama, alamat, no_hp FROM pelanggan WHERE id = %s"
    cursor.execute(query, (customer_id,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None


def fetch_all_customers():
    cursor = get_cursor()
    query = "SELECT id, nama, alamat, no_hp FROM pelanggan"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


def fetch_customer_order_details(customer_id):
    cursor = get_cursor()

    query = """
    SELECT 
        p.id AS customer_id, p.nama AS customer_name,
        pm.id AS order_id, pm.status_pesanan, pm.pesanan_dibuat, pm.metode_pembayaran, pm.total_harga,
        pg.pengiriman_selesai,
        k.nama AS courier_name, k.kendaraan,
        u.rating, u.komentar
    FROM pelanggan p
    JOIN pesanan pm ON p.id = pm.id_pelanggan
    LEFT JOIN pengiriman pg ON pm.id = pg.id_pesanan
    LEFT JOIN kurir k ON pg.id_kurir = k.id
    LEFT JOIN ulasan u ON pm.id = u.id_pesanan
    WHERE p.id = %s
    ORDER BY pm.pesanan_dibuat DESC
    """
    cursor.execute(query, (customer_id,))
    result = cursor.fetchall()
    cursor.close()
    return result


def insert_customer(name, address, phone):
    cursor = get_cursor()
    query = "INSERT INTO pelanggan (nama, alamat, no_hp) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (name, address, phone))
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print(f"\n[Database Error]: {e}")
        return False
    finally:
        cursor.close()


def update_customer(customer_id, name, address, phone):
    cursor = get_cursor()
    query = """
    UPDATE pelanggan 
    SET nama = %s, alamat = %s, no_hp = %s 
    WHERE id = %s
    """
    try:
        cursor.execute(query, (name, address, phone, customer_id))
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        print(f"\n[Database Error]: {e}")
        return False
    finally:
        cursor.close()
