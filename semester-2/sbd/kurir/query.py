from db import db, get_cursor


def fetch_courier_by_id(courier_id):
    cursor = get_cursor()
    try:
        query = (
            "SELECT id, nama, status_ketersediaan, kendaraan FROM kurir WHERE id = %s"
        )
        cursor.execute(query, (courier_id,))
        result = cursor.fetchone()
        return result is not None
    except Exception as e:
        print(f"\n[Database Error]: Gagal mengecek ID kurir. {e}")
        return False
    finally:
        cursor.close()


def fetch_all_couriers():
    cursor = get_cursor()
    try:
        query = """
        SELECT id, nama, 
               CASE WHEN status_ketersediaan = 1 THEN 'Available' ELSE 'Unavailable' END, 
               kendaraan 
        FROM kurir
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"\n[Database Error]: Gagal mengambil semua data kurir. {e}")
        return []
    finally:
        cursor.close()


def insert_courier(name, vehicle):
    cursor = get_cursor()
    query = "INSERT INTO kurir (nama, kendaraan) VALUES (%s, %s)"
    try:
        cursor.execute(query, (name, vehicle))
        db.commit()
        return True
    except Exception as error:
        db.rollback()
        print(f"\n[Database Error]: Gagal menambah kurir baru. {error}")
        return False
    finally:
        cursor.close()


def update_courier(courier_id, name, vehicle):
    cursor = get_cursor()
    query = """
    UPDATE kurir 
    SET nama = %s, kendaraan = %s 
    WHERE id = %s
    """
    try:
        cursor.execute(query, (name, vehicle, courier_id))
        db.commit()
        return True
    except Exception as error:
        db.rollback()
        print(f"\n[Database Error]: Gagal memperbarui data kurir. {error}")
        return False
    finally:
        cursor.close()
