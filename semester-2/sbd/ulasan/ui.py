from tabulate import tabulate

from ulasan.query import fetch_completed_orders_without_review, insert_review


def form_add_review():
    print("=========================================")
    print("           BERI ULASAN PESANAN           ")
    print("=========================================")

    orders = fetch_completed_orders_without_review()
    if not orders:
        print("\n[Info] Tidak ada pesanan selesai yang belum diulas.")
        return

    headers = ["ID Pesanan", "ID Pelanggan", "Tanggal Selesai", "Total Harga (Rp)"]
    print("\n=== DAFTAR PESANAN SELESAI ===")
    print(tabulate(orders, headers=headers, tablefmt="grid"))

    try:
        id_pesanan = int(input("\nMasukkan ID Pesanan yang ingin diulas: "))
        rating = int(input("Masukkan Rating (1-5): "))
        if rating < 1 or rating > 5:
            print("[Error] Rating harus antara 1 sampai 5!")
            return
        
        komentar = input("Masukkan Komentar: ").strip()
        if not komentar:
            print("[Error] Komentar tidak boleh kosong!")
            return
            
    except ValueError:
        print("[Error] Input ID Pesanan dan Rating harus berupa angka!")
        return

    success = insert_review(id_pesanan, rating, komentar)
    if success:
        print(f"\n[Sukses] Berhasil menambahkan ulasan untuk ID Pesanan {id_pesanan}.")
    else:
        print(f"\n[Gagal] Gagal menambahkan ulasan. Pastikan ID Pesanan benar dan sudah selesai.")
