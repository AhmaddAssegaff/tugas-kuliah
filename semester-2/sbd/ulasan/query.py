from db import db, get_cursor


def insert_review(id_pesanan, rating, komentar):
    cursor = get_cursor()
    try:
        query = """
        INSERT INTO ulasan (id_pesanan, rating, komentar)
        SELECT id, %s, %s
        FROM pesanan
        WHERE id = %s
          AND status_pesanan = TRUE
        """

        cursor.execute(query, (rating, komentar, id_pesanan))
        db.commit()

        return cursor.rowcount > 0

    except Exception as e:
        db.rollback()
        print(f"\n[Database Error]: {e}")
        return False
    finally:
        cursor.close()


def fetch_completed_orders_without_review():
    cursor = get_cursor()
    try:
        # Fetch orders that are completed but don't have a review yet
        query = """
            SELECT p.id, p.id_pelanggan, p.pesanan_dibuat, p.total_harga
            FROM pesanan p
            LEFT JOIN ulasan u ON p.id = u.id_pesanan
            WHERE p.status_pesanan = TRUE AND u.id IS NULL
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"\n[Database Error]: {e}")
        return []
    finally:
        cursor.close()
