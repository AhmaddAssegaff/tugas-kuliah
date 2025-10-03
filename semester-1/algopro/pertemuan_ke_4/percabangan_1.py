usr_inp = int(input("masukkan nilai angka : "))
sisa_bagi_2 = usr_inp % 2

if sisa_bagi_2 == 0:
    print(f"{usr_inp} adalah angka : genap")
else:
    print(f"{usr_inp} adalah angka : ganjil")