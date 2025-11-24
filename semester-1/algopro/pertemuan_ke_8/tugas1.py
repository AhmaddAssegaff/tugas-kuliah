def menu():
    print(""" DAFTAR MENU
    1. volume balok
    2. volume kubus
    3. volume bola
    """)
    pilihan = int(input("masukkan pilihan anda : "))
    if pilihan == 1:
        volume_balok()
    elif pilihan == 2:
        volume_kubus()
    elif pilihan == 3:
        volume_bola()
    else:
        print("err")

def volume_balok():
    panjang = int(input("masukkan Panjangn Balok : "))
    lebar = int(input("masukkan lebar Balok : "))
    tinggi = int(input("masukkan tinggi Balok : "))
    rumus = panjang*lebar*tinggi
    print(rumus)
    pilihan_lain = input("apakah ingin memilih manu lain : (y/n)")
    if pilihan_lain == "y":
        menu()
    else:
        print("program berakhir")


def volume_kubus():
    sisi = int(input("masukkan sisi kubus : "))
    rumus = sisi ** 3
    print(rumus)
    pilihan_lain = input("apakah ingin memilih manu lain : (y/n)")
    if pilihan_lain == "y":
        menu()
    else:
        print("program berakhir")


def volume_bola():
    jari = int(input("masukkan jari-jari bola : "))
    rumus = 3/4 * 3.14 * (jari ** 3)
    print(rumus)
    pilihan_lain = input("apakah ingin memilih manu lain : (y/n)")
    if pilihan_lain == "y":
        menu()
    else:
        print("program berakhir")

menu()
