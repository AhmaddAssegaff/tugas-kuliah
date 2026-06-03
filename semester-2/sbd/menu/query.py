from db import db, get_cursor


def fetch_menu_by_id(menu_id):
    cursor = get_cursor()
    try:
        query = "SELECT id, nama, harga, stock FROM menu WHERE id = %s"
        cursor.execute(query, (menu_id,))
        return cursor.fetchone()
    except Exception as e:
        print(f"\n[Database Error]: Gagal mengambil menu berdasarkan ID. {e}")
        return None
    finally:
        cursor.close()


def fetch_all_menus():
    cursor = get_cursor()
    try:
        query = "SELECT id, nama, harga, stock FROM menu"
        cursor.execute(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"\n[Database Error]: Gagal mengambil semua data menu. {e}")
        return []
    finally:
        cursor.close()


def insert_menu(name, price, stock):
    cursor = get_cursor()
    query = "INSERT INTO menu (nama, harga, stock) VALUES (%s, %s, %s)"
    try:
        cursor.execute(query, (name, price, stock))
        db.commit()
        return True
    except Exception as error:
        db.rollback()
        print(f"\n[Database Error]: Gagal menambah menu baru. {error}")
        return False
    finally:
        cursor.close()


def update_menu(menu_id, name, price, stock):
    cursor = get_cursor()
    query = """
    UPDATE menu
    SET nama = %s, harga = %s, stock = %s
    WHERE id = %s
    """
    try:
        cursor.execute(query, (name, price, stock, menu_id))
        db.commit()
        return True
    except Exception as error:
        db.rollback()
        print(f"\n[Database Error]: Gagal memperbarui data menu. {error}")
        return False
    finally:
        cursor.close()
