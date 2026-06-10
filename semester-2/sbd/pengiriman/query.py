from db import db, get_cursor


def fetch_all_delivery():
    cursor = get_cursor()
    try:
        query = """
            SELECT 
                p.id AS id_pengiriman,
                p.id_pesanan,
                k.nama AS nama_kurir,
                pl.nama AS nama_pelanggan,
                p.status,
                p.pengiriman_selesai
            FROM pengiriman p
            JOIN kurir k ON p.id_kurir = k.id
            JOIN pesanan pes ON p.id_pesanan = pes.id
            JOIN pelanggan pl ON pes.id_pelanggan = pl.id
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"\n[Database Error]: Gagal mengambil data pengiriman. {e}")
        return []
    finally:
        cursor.close()


def fetch_all_order_ready_to_deliver():
    cursor = get_cursor()
    try:
        query = """
            SELECT
                p.id,
                pl.nama,
                p.metode_pembayaran,
                p.total_harga
            FROM pesanan p
            JOIN pelanggan pl ON pl.id = p.id_pelanggan
            LEFT JOIN pengiriman pg ON pg.id_pesanan = p.id
            WHERE p.status_pesanan = TRUE
            AND pg.id IS NULL
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"\n[Database Error]: Gagal mengambil data pesanan siap kirim. {e}")
        return []
    finally:
        cursor.close()


def fetch_all_delivery_on_progress():
    cursor = get_cursor()
    try:
        query = """
            SELECT
                p.id,
                pl.nama,
                p.metode_pembayaran,
                p.total_harga
            FROM pesanan p
            JOIN pelanggan pl ON pl.id = p.id_pelanggan
            JOIN pengiriman pg ON pg.id_pesanan = p.id
            WHERE pg.status = 'dikirim'
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"\n[Database Error]: Gagal mengambil data pengiriman aktif. {e}")
        return []
    finally:
        cursor.close()


def create_delivery(id_pesanan, id_kurir):
    cursor = get_cursor()
    try:
        cursor.execute(
            "INSERT INTO pengiriman (id_pesanan, id_kurir) VALUES (%s, %s)",
            (id_pesanan, id_kurir),
        )
        db.commit()
        return cursor.rowcount > 0
    except Exception as e:
        db.rollback()
        print(f"\n[Database Error]: Gagal membuat pengiriman. {e}")
        return False
    finally:
        cursor.close()


def finish_delivery(id_pesanan):
    cursor = get_cursor()
    try:
        cursor.execute(
            """
            UPDATE pengiriman
            SET status = 'selesai dikirim', pengiriman_selesai = NOW()
            WHERE id_pesanan = %s AND status = 'dikirim'
            """,
            (id_pesanan,),
        )
        db.commit()
        return cursor.rowcount > 0
    except Exception as e:
        db.rollback()
        print(f"\n[Database Error]: Gagal menyelesaikan pengiriman. {e}")
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
