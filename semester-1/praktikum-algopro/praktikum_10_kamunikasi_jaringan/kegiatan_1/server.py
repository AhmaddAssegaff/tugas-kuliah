import socket 

host = 'localhost'
port = 5003

data = {
    'nama' : 'Ahmad',
    'NIM' : 'L200250034',
    'angkatan': 2025,
}

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

    if pesan_user in data:
        client.send(str(data[pesan_user]).encode())
        print(f"respones : {data[pesan_user]}")
    else:
        client.send(b"Perintah tidak dikenal")

    client.close()

server.close()
print("Server OFF.")
