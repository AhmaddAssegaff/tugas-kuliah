from db import get_cursor
from menu.query import decrease_menu_stock


def insert_customer_order(
    id_pelanggan, metode_pembayaran, total_harga, list_detail_pesanan
):
    cursor = get_cursor()
    try:
        q_order = "INSERT INTO pesanan (id_pelanggan, metode_pembayaran, total_harga) VALUES (%s, %s, %s)"
        cursor.execute(q_order, (id_pelanggan, metode_pembayaran, total_harga))

        id_pesanan_baru = cursor.lastrowid

        vals_detail = []
        for item in list_detail_pesanan:
            vals_detail.append(
                (
                    id_pesanan_baru,
                    item["id_menu"],
                    item["kuantitas"],
                    item["sub_total"],
                    item["harga_menu_saat_pesan"],
                )
            )
            decrease_menu_stock(item["id_menu"], item["kuantitas"])

        q_detail = """
            INSERT INTO detail_pesanan (id_pesanan, id_menu, kuantitas, sub_total, harga_menu_saat_pesan)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.executemany(q_detail, vals_detail)
        return id_pesanan_baru

    except Exception as e:
        print(f"\n[Error] Gagal menyimpan pesanan ke database: {e}")
        return None
    finally:
        cursor.close()
