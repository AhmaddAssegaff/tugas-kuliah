nama = "Ahmad"
tanggal_lahir = "12-06-2006"
nim = "L200250034"

berkas = open("L200250034", "w")
berkas.write(nim + "\n")
berkas.write(tanggal_lahir + "\n")
berkas.write(nama + "\n")
berkas.close()

berkas = open("L200250034", "r")
isi_berkas = berkas.read()
print(isi_berkas)
berkas.close()
