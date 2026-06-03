# pesanan/ui.py
from menu.ui import display_menus

# Import fungsi display dari folder modul lain yang sudah kamu buat
from pelanggan.ui import display_customers
from pesanan.query import insert_customer_order


def form_create_order():
    print("=========================================")
    print("           CREATE NEW ORDER              ")
    print("=========================================")

    # 1. TAMPILKAN DAFTAR PELANGGAN TERLEBIH DAHULU
    print("\n--- DAFTAR PELANGGAN TERSEDIA ---")
    display_customers()
    print("---------------------------------")

    # Baru minta input ID Pelanggan setelah mereka melihat daftarnya
    try:
        id_pelanggan = int(input("\nMasukkan ID Pelanggan dari daftar di atas: "))
    except ValueError:
        print("[Error] ID Pelanggan harus berupa angka!")
        return

    metode_pembayaran = (
        input("Metode Pembayaran (CASH/QRIS/TRANSFER): ").strip().upper()
    )

    # List penampung item / keranjang belanja di memori UI
    keranjang_belanja = []
    total_harga_pesanan = 0

    # 2. TAMPILKAN DAFTAR MENU SEKALI DI AWAL SEBELUM INPUT ITEM
    print("\n--- DAFTAR MENU TERSEDIA ---")
    display_menus()
    print("----------------------------")
    print("*(Masukkan 0 pada ID Menu jika semua pesanan selesai diinput)")

    while True:
        try:
            print(f"\n[Item ke-{len(keranjang_belanja) + 1}]")
            id_menu = int(input("Masukkan ID Menu: "))
            if id_menu == 0:
                break

            kuantitas = int(input("Kuantitas / Jumlah: "))
            harga_satuan = int(input("Harga Menu Saat Ini (Rp): "))
        except ValueError:
            print("[Error] Input harus berupa angka! Silakan ulangi item ini.")
            continue

        # Hitung subtotal per item
        sub_total = kuantitas * harga_satuan
        total_harga_pesanan += sub_total

        # Simpan ke keranjang belanja per item
        item_baru = {
            "id_menu": id_menu,
            "kuantitas": kuantitas,
            "harga_menu_saat_pesan": harga_satuan,
            "sub_total": sub_total,
        }
        keranjang_belanja.append(item_baru)
        print(f"-> Berhasil menambahkan item ke keranjang. Subtotal: Rp {sub_total:,}")

    # Validasi jika kasir langsung keluar tanpa mengisi menu apapun
    if not keranjang_belanja:
        print("\n[Batal] Pesanan tidak diproses karena keranjang kosong.")
        return

    # Tampilkan rangkuman ringkas sebelum submit ke database
    print("\n==============================")
    print("       RANGKUMAN PESANAN      ")
    print("==============================")
    print(f"Total Jenis Item : {len(keranjang_belanja)}")
    print(f"Total Bayar      : Rp {total_harga_pesanan:,}")
    print("==============================")
    konfirmasi = input("Simpan transaksi ini ke database? (y/n): ").strip().lower()

    if konfirmasi == "y":
        # Panggil query dengan melemparkan list data utuh
        id_nota = insert_customer_order(
            id_pelanggan=id_pelanggan,
            metode_pembayaran=metode_pembayaran,
            total_harga=total_harga_pesanan,
            list_detail_pesanan=keranjang_belanja,
        )
        if id_nota:
            print(f"\n[Sukses] Pesanan berhasil disimpan dengan ID Pesanan: {id_nota}")
    else:
        print("\n[Batal] Transaksi dibatalkan oleh pengguna.")
