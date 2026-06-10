from pengiriman.query import (
    create_delivery,
    fetch_all_couriers,
    fetch_all_delivery,
    fetch_all_delivery_on_progress,
    fetch_all_order_ready_to_deliver,
    finish_delivery,
)
from tabulate import tabulate


def display_all_delivery():
    print("\n=== DATA SEMUA PENGIRIMAN ===")
    data = fetch_all_delivery()
    headers = [
        "ID Kirim",
        "ID Pesan",
        "Nama Kurir",
        "Nama Pelanggan",
        "Status",
        "Waktu Selesai",
    ]
    if data:
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
    else:
        print("[ Data Pengiriman Kosong ]")


def display_order_ready_to_deliver():
    print("\n=== PESANAN SIAP DIKIRIM ===")
    data = fetch_all_order_ready_to_deliver()
    headers = ["ID Pesanan", "Nama Pelanggan", "Metode Pembayaran", "Total Harga (Rp)"]
    if data:
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
        return True
    else:
        print("[ Tidak ada pesanan yang siap dikirim ]")
        return False


def display_couriers():
    couriers = fetch_all_couriers()
    if not couriers:
        print("\nNo courier data found.")
        return
    print("\n=== COURIER LIST ===\n")
    print(
        tabulate(couriers, headers=["ID", "Name", "Status", "Vehicle"], tablefmt="grid")
    )


def display_delivery_on_progress():
    print("\n=== PENGIRIMAN SEDANG BERJALAN ===")
    data = fetch_all_delivery_on_progress()
    headers = ["ID Pesanan", "Nama Pelanggan", "Metode Pembayaran", "Total Harga (Rp)"]
    if data:
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
        return True
    else:
        print("[ Tidak ada pengiriman yang sedang berjalan ]")
        return False


def form_create_delivery():
    print("=========================================")
    print("           BUAT PENGIRIMAN BARU          ")
    print("=========================================")

    ada_data_order = display_order_ready_to_deliver()
    ada_data_kurir = display_couriers()

    if not ada_data_order:
        input("\nTekan Enter untuk kembali ke menu...")
        return

    if not ada_data_kurir:
        input("\nTekan Enter untuk kembali ke menu...")
        return

    try:
        id_pesanan = int(input("\nMasukkan ID Pesanan yang ingin dikirim: "))
        id_kurir = int(input("Masukkan ID Kurir: "))
    except ValueError:
        print("[Error] ID harus berupa angka!")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    berhasil = create_delivery(id_pesanan, id_kurir)
    if berhasil:
        print(f"\n[SUKSES] Pengiriman untuk pesanan ID {id_pesanan} berhasil dibuat!")
    else:
        print("\n[GAGAL] Gagal membuat pengiriman. Periksa ID Pesanan dan ID Kurir.")

    input("\nTekan Enter untuk kembali ke menu...")


def form_finish_delivery():
    print("=========================================")
    print("         KONFIRMASI SELESAI KIRIM        ")
    print("=========================================")

    ada_data = display_delivery_on_progress()
    if not ada_data:
        input("\nTekan Enter untuk kembali ke menu...")
        return

    try:
        id_pesanan = int(input("\nMasukkan ID Pesanan yang sudah selesai dikirim: "))
    except ValueError:
        print("[Error] ID harus berupa angka!")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    konfirmasi = (
        input(f"Yakin pesanan ID {id_pesanan} sudah selesai dikirim? (y/n): ")
        .strip()
        .lower()
    )

    if konfirmasi == "y":
        berhasil = finish_delivery(id_pesanan)
        if berhasil:
            print(
                f"\n[SUKSES] Pesanan ID {id_pesanan} berhasil dikonfirmasi selesai dikirim!"
            )
        else:
            print("\n[GAGAL] ID Pesanan tidak ditemukan atau sudah selesai sebelumnya.")
    else:
        print("\n[BATAL] Konfirmasi dibatalkan.")

    input("\nTekan Enter untuk kembali ke menu...")
