class volume_bangunan():
    def menu(self):
        print(""" DAFTAR MENU
        1. volume balok
        2. volume kubus
        3. volume bola
        """)
        pilihan = int(input("masukkan pilihan anda : "))
        if pilihan == 1:
            self.volume_balok()
        elif pilihan == 2:
            self.volume_kubus()
        elif pilihan == 3:
            self.volume_bola()
        else:
            print("err")

    def volume_balok(self):
        panjang = int(input("masukkan Panjangn Balok : "))
        lebar = int(input("masukkan lebar Balok : "))
        tinggi = int(input("masukkan tinggi Balok : "))
        rumus = panjang*lebar*tinggi
        print(rumus)
        pilihan_lain = input("apakah ingin memilih manu lain : (y/n)")
        if pilihan_lain == "y":
            self.menu()
        else:
            print("program berakhir")


    def volume_kubus(self):
        sisi = int(input("masukkan sisi kubus : "))
        rumus = sisi ** 3
        print(rumus)
        pilihan_lain = input("apakah ingin memilih manu lain : (y/n)")
        if pilihan_lain == "y":
            self.menu()
        else:
            print("program berakhir")


    def volume_bola(self):
        jari = int(input("masukkan jari-jari bola : "))
        rumus = 3/4 * 3.14 * (jari ** 3)
        print(rumus)
        pilihan_lain = input("apakah ingin memilih manu lain : (y/n)")
        if pilihan_lain == "y":
            self.menu()
        else:
            print("program berakhir")

app = volume_bangunan()
app.menu()
