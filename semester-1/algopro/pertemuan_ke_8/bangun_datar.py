def menu():
    print (""" ============ BANGUN DATAR ============
1. Persegi, 
2. Persegi Panjang,
3. Segitiga
    """)
    pilihan = int(input("Silakan pilih menu Bangun Datar: "))
    if pilihan == 1:
        persegi()
    elif pilihan == 2:
        persegi_panjang()
    elif pilihan == 3:
        segitiga()
    else:
        print ("Pilihan anda salah")

def persegi():
    print ("======= Menu Persegi =========")
    sisi = int(input("Masukkan panjang sisi: "))
    rumus = sisi*sisi
    print ("Luas Persegi adalah ", rumus)
    pilihan = input("Apakah ingin memilih luas bangun datar yang lain (YA/TIDAK)")
    if pilihan.upper() == "YA":
        menu()
    else:
        print ("Program Berakhir")

def persegi_panjang():
    print ("======= Menu Persegi Panjang =========")
    panjang = int(input("Masukkan panjang panjang: "))
    lebar = int(input("Masukkan panjang lebar: "))
    rumus = panjang*lebar
    print ("Luas Persegi Panjang adalah ", rumus)
    pilihan = input("Apakah ingin memilih luas bangun datar yang lain (YA/TIDAK)")
    if pilihan.upper() == "YA":
        menu()
    else:
        print ("Program Berakhir")

def segitiga():
    print ("======= Menu Segitiga =========")
    alas = int(input("Masukkan panjang alas: "))
    tinggi = int(input("Masukkan panjang tinggi: "))
    rumus = 0.5*alas*tinggi
    print ("Luas segita adalah ", rumus)
    pilihan = input("Apakah ingin memilih luas bangun datar yang lain (YA/TIDAK)")
    if pilihan.upper() == "YA":
        menu()
    else:
        print ("Program Berakhir")

menu()