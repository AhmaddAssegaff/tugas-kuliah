nama = "Ahmada"
nim = 200250034
tinggi_badan = 1.60
berat = 62
tahun_lahir = 2006

aku = [tahun_lahir, berat, tinggi_badan, nim, nama]
data = [tahun_lahir, berat, tinggi_badan, nim, nama]

print(type(aku))
print(aku[0])

a = nim % 4; aku[a]

print(aku[0])
print(aku[a:4])
print(type(aku[4]))

aku[0] = 'ok'

print(type(data))
print(type(data[4]))
print(type(data[4][5]))
print(type(data[4][a:6]))

data[0] = "ok"

print(data[-a])
print(data[a])