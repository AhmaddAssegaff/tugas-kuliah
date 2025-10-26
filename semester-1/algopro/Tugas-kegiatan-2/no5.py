print("Program menghitung jumlah bilangan negatif.")
print("Dibuat oleh Ahmad")

bilangan = [1, 2, -3, 4, -5, 6, 7, 8, -9, 10, 11, 12]
bilangan_negatif = 0

for angka in bilangan:
    if angka < 0:
        bilangan_negatif += 1

print("total bilangan negatif", bilangan_negatif)