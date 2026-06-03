from query import ambil_kurir, ambil_pelanggan, ambil_pesanan_pelanggan
from tabulate import tabulate


def tampilkan_pelanggan():
    pelanggan = ambil_pelanggan()

    if not pelanggan:
        print("Belum ada data pelanggan")
        return

    print("\nDAFTAR PELANGGAN\n")

    print(
        tabulate(
            pelanggan,
            headers=[
                "ID",
                "Nama",
                "Alamat",
                "Nomor HP",
            ],
            tablefmt="grid",
        )
    )


def tampilkan_detail_pelanggan():
    tampilkan_pelanggan()

    id_pelanggan = input("\nMasukkan ID pelanggan: ")

    pesanan = ambil_pesanan_pelanggan(id_pelanggan)

    if not pesanan:
        print("\nPesanan tidak ditemukan")
        return

    print("\nDAFTAR PESANAN\n")

    print(
        tabulate(
            pesanan,
            headers=[
                "ID Pelanggan",
                "Nama",
                "ID Pesanan",
                "Status",
                "Tanggal Pesan",
                "Pembayaran",
                "Total",
                "Estimasi Kirim",
                "Kurir",
                "Kendaraan",
                "Rating",
                "Komentar",
            ],
            tablefmt="grid",
        )
    )


def tampilkan_kurir():
    kurir = ambil_kurir()

    if not kurir:
        print("\n Kurir idak ditemukan")
        return

    print("\nDAFTAR KURIR\n")

    print(
        tabulate(
            kurir,
            headers=["ID Kurir", "Nama", "Status ketersediaan", "Kendaraan"],
            tablefmt="grid",
        )
    )
