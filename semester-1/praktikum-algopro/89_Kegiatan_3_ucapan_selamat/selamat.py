name = input("masukkan nama anda :")
timeNow = int(input("pukul berapa sekarang :"))

time_list = [
    ((0, 10), "pagi"),
    ((10, 15), "siang"),
    ((15, 18), "sore"),
    ((18, 21), "petang"),
    ((21, 24), "malam"),
]

sapaan = None
for (start, end), label in time_list:
    # print(start, end, label)
    if start <= timeNow < end:
        sapaan = label
        break

if sapaan:
    print(f"Selamat {sapaan}, {name}!")
else:
    print("Jam tidak valid.")