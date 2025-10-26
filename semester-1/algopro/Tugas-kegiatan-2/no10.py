print("Program menghitung angka terkecil.")
print("Dibuat oleh Ahmad")

angka_terkecil = 0

for i in range(1, 9):
    angka = int(input(f"masukkan angka anda yang ke-{i}: "))
    if angka == 1:
        angka_terkecil = angka
    elif angka < angka_terkecil:
        angka_terkecil = angka
print("angka terkecil adalah : ", angka_terkecil)
