bangun_datar={
    "segtiga": "L = 0.5 * a * t",
    "Persegi": "s ** 2",
    "Persegi Panjang": "p * l",
    "Lingkaran": "π * r * r",
    "Jajar Genjang": "a * t",
}

print("-"*50)
print(f"{'No ': <5} | {'Nama Bangun Datar':20} | {'Rumus Luas':20}")
print("-"*50)

for index, (nama, rumus) in enumerate(bangun_datar.items(), start=1):
    print(f"{index:<5} | {nama:20} | {rumus:20}")

print("=" *50)
