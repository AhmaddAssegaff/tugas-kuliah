
import socket

host = "127.0.0.1"
port = 5003

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
