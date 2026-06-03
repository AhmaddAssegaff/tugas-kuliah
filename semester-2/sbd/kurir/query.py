from db import get_cursor


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
