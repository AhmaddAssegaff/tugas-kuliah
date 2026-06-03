from db import db, get_cursor


def fetch_courier_by_id(courier_id):
    cursor = get_cursor()
    query = "SELECT id, nama, status_ketersediaan, kendaraan FROM kurir WHERE id = %s"
    cursor.execute(query, (courier_id,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None


def fetch_all_couriers():
    cursor = get_cursor()
    query = """
    SELECT id, nama, 
           CASE WHEN status_ketersediaan = 1 THEN 'Available' ELSE 'Unavailable' END, 
           kendaraan 
    FROM kurir
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


def insert_courier(name, vehicle):
    cursor = get_cursor()
    query = "INSERT INTO kurir (nama, kendaraan) VALUES (%s, %s)"

    try:
        cursor.execute(query, (name, vehicle))
        db.commit()
        return True
    except Exception as error:
        db.rollback()
        print(f"\n[Database Error]: {error}")
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
        print(f"\n[Database Error]: {error}")
        return False
    finally:
        cursor.close()
