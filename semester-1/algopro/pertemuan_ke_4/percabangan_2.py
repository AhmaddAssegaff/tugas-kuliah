usr_inp = int(input("masukkan umur anda : "))
under_18 = usr_inp < 18
under_10 = usr_inp < 10

if under_10:
    print("tidak dilarang melilih anda under age")
elif under_18:
    print("anda hanya boleh memilih a b c")
else:
    print("anda serior citizen")