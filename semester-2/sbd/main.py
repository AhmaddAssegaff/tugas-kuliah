import os

from db import close_connection
from tampilan import tampilkan_detail_pelanggan, tampilkan_kurir, tampilkan_pelanggan


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    while True:
        clear_screen()

        print("========================")
        print(" SISTEM KASIR SEDERHANA ")
        print("========================")
        print("1. Lihat Pelanggan")
        print("2. Detail Pesanan Pelanggan")
        print("3. Lihat Kurir")
        print("0. Keluar")

        pilihan = input("\nPilih menu: ")

        if pilihan == "1":
            clear_screen()
            tampilkan_pelanggan()
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan == "2":
            clear_screen()
            tampilkan_detail_pelanggan()
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan == "3":
            clear_screen()
            tampilkan_kurir()
            input("\nTekan Enter untuk kembali ke menu...")

        elif pilihan == "0":
            clear_screen()
            close_connection()
            print("Terima kasih")
            break

        else:
            print("\nMenu tidak tersedia")
            input("\nTekan Enter untuk lanjut...")


if __name__ == "__main__":
    menu()
