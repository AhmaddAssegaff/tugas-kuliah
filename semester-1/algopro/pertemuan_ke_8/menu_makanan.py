def menu():
    print(""" ====== MENU MAKANAN ======
    1. Bakmi Goreng - Rp 20.000
    2. Mie Ayam     - Rp 15.000
    3. Bakso        - Rp 15.000
    """)
    harga_menu()

def harga_menu():
    menu1 = "Bakmi Goreng"
    harga1 = 20000
    menu2 = "Mie Ayam"
    harga2 = 15000
    menu3 = "Bakso"
    harga3 = 15000
    pilihan = int(input("masukkan piliahn menu: "))
    
    if pilihan == 1:
        menu1, harga1
        porsi = int(input("Masukkan jumlah porsi yang dipesan: "))
        tampilkan_receipt (menu1, harga1, porsi)
    
    if pilihan == 2:
        menu2, harga2
        porsi = int(input("Masukkan jumlah porsi yang dipesan: "))
        tampilkan_receipt (menu2, harga2, porsi)
    
    if pilihan == 3:
        menu3, harga3
        porsi = int(input("Masukkan jumlah porsi yang dipesan: "))
        tampilkan_receipt (menu3, harga3, porsi)
    
    else:
        print ("Pilihan anda salah")

def tampilkan_receipt(nama_makanan, harga, porsi):
    total = harga * porsi
    print (f"""
    ========== RECEIPT ================
    Menu    : {nama_makanan}
    Harga   : {harga}
    Porsi   : {porsi}
    -----------------------------
    Total Bayar: Rp {total}
    """)

menu()