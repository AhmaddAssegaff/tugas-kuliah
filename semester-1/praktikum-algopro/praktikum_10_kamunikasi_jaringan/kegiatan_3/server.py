import socket 

host = 'localhost'
port = 5006

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

while True:
    client, addr = server.accept()
    print(f"client datang : ${addr}")

    pesan_user = client.recv(1024).decode().strip()
    print(f"Perintah dari client : {pesan_user}")

    if pesan_user == 'q':
        client.send(b"Server dihentikan.")
        client.close()
        running = False
        break

    def persegi(params):
         return params * params

    if pesan_user == "hitung_persegi":
        client.send(b"Masukkan sisi: ")

        sisi = client.recv(1024).decode().strip()

        try:
            sisi = int(sisi)
            hasil = persegi(sisi)
            client.send(f"Hasil persegi: {hasil}".encode())
        except:
            client.send(b"Input sisi tidak valid.")
    else:
        client.send(b"Perintah tidak dikenal")

    client.close()

server.close()
print("Server OFF.")
