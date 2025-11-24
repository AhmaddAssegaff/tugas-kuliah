import shelve

berkas = open("L200250034", "r")
isi_berkas = berkas.read()
berkas.close()

F = shelve.open("ahmad")
F["data"] = isi_berkas
F.close()
