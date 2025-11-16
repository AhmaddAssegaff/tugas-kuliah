data = {
    "nama": "ahmad",
    "nim": "L200250034",
    "alamat": "dimana yak",
    "umur": 19,
    "nik": "bla bla bla",
    "univ": "yuemes",
    "fakultas": "FKI",
}

mapping = {
    "n": "nama",
    "i": "nim",
    "a": "alamat",
    "u": "umur",
    "k": "nik",
    "v": "univ",
    "f": "fakultas",
}
print(mapping)


def ambil_data():
    pilihan = input("pilih Kode untuk menampilkan data sesuai pilihan :")
    if pilihan in mapping:
        print(data[mapping[pilihan]])
    else:
        print("Kode tidak ditemukan")
