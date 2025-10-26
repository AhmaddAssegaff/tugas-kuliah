print("Program menampilkan bilangan ganjil.")
print("Dibuat oleh Ahmad")

user_input_1 = int(input("Masukkan bilangan awal: "))
user_input_2 = int(input("Masukkan bilangan akhir: "))

bilangan = user_input_1

print(f"Bilangan ganjil antara {user_input_1} dan {user_input_2}:")

while bilangan <= user_input_2:
    if bilangan % 2 != 0:
        print(bilangan, end=" ")
    bilangan += 1
