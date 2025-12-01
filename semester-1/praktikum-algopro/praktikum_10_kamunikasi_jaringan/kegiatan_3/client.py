import socket

host = "localhost"
port = 5001

while True:
    pesan = input("Masukkan perintah (atau 'q' untuk quit): ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    client.send(pesan.encode())

    balasan = client.recv(1024).decode()
    print("Balasan server:", balasan)

    if pesan == "hitung_persegi":
        sisi = input("Isi sisi: ")
        client.send(sisi.encode())

        hasil = client.recv(1024).decode()
        print("Hasil:", hasil)

    client.close()

    if pesan == 'q':
        break
