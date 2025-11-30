
import socket

host = "localhost"
port = 5004

while True:
    pesan = input("Masukkan perintah (atau 'q' untuk quit): ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    client.send(pesan.encode())

    balasan = client.recv(1024).decode()
    print("Balasan server:", balasan)

    client.close()

    if pesan == 'q':
        break
