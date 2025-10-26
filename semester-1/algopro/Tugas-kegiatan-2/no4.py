print("Program menghitung kata dalam kalimat.")
print("Dibuat oleh Ahmad")

kalimat_user = input("masukkan kalimat anda: ")
split_kalimat_user = kalimat_user.split()
kalimat_user = 0

for kata in split_kalimat_user:
    kalimat_user += 1

print("total kalimat dari user", kalimat_user)