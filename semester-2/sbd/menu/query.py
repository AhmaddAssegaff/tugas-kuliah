from db import db, get_cursor


def fetch_menu_by_id(courier_id):
    cursor = get_cursor()
    query = "SELECT id, nama, harga, stock FROM menu WHERE id = %s"
    cursor.execute(query, (courier_id,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None


def fetch_all_menus():
    cursor = get_cursor()
    query = """
    SELECT id, nama, harga, stock  FROM menu
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result


def insert_menu(name, price, stock):
    cursor = get_cursor()
    query = "INSERT INTO menu (nama, harga, stock) VALUES (%s, %s, %s)"

    try:
        cursor.execute(query, (name, price, stock))
        db.commit()
        return True
    except Exception as error:
        db.rollback()
        print(f"\n[Database Error]: {error}")
        return False
    finally:
        cursor.close()


def update_menu(name, price, stock):
    cursor = get_cursor()
    query = """
    UPDATE menu
    SET nama = %s, harga = %s, stock = %s
    WHERE id = %s
    """
    try:
        cursor.execute(query, (name, price, stock))
        db.commit()
        return True
    except Exception as error:
        db.rollback()
        print(f"\n[Database Error]: {error}")
        return False
    finally:
        cursor.close()
