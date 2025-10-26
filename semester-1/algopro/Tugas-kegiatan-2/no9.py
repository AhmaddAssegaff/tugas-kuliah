print("Program menghitung jumlah bilangan negatif.")
print("Dibuat oleh Ahmad")

print("Program menampilkan kelipatan 3 antara bilangan awal dan akhir.")
print("Dibuat oleh Ahmad Asgf")

awal = int(input("Masukkan bilangan awal: "))
akhir = int(input("Masukkan bilangan akhir: "))

print(f"Kelipatan 3 antara {awal} dan {akhir}:", end=" ")

bilangan = awal

while bilangan <= akhir:
    if bilangan % 3 == 0:
        print(bilangan, end=" ")
    bilangan += 1