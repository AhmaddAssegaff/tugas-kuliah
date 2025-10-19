# # TUGAS NO 1 print ganjil dengan dengan range dari input
# nilai_akhir_1 = int(input("masukkan nilai max untuk print ganjil :"))
# for index in range(1, nilai_akhir_1, 2):
#     print(f"angka ganjil : {index}")

# nilai_akhir_2 = int(input("masukkan nilai max untuk print genap :"))
# for index in range(2, nilai_akhir_2, 2):
#     print(f"angka genap : {index}")

# # TUGAS NO 2 segitiga siku-siku dengan bintang
# banyak_baris = int(input("masukkan seberapa banyak baris: "))
# banyak_bintang = int(input("banyak bintnag yg di inginkan :"))

# # segitiga siku siku
# for i in range(1, banyak_bintang + 1):
#     for i in range(1, banyak_baris -1):
#         print("*" * i)
#     print()
    
# # segitiga sama sisi
# for i in range(1, banyak_bintang + 1):
#     for x in range(1, 1+ banyak_baris):
#         print(' ' * (banyak_baris - x) + '*' * (2 * x - 1))
#     print()


# TUGAS NO 3 Fibonacci
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(10))
