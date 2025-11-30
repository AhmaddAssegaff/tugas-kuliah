import socket 
import platform

host = 'localhost'
port = 5004

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

running = True

while running:
    client, addr = server.accept()
    print(f"client datang : ${addr}")

    pesan_user = client.recv(1024).decode().strip()
    print(f"Perintah dari client : {pesan_user}")

    if pesan_user == 'q':
        client.send(b"Server dihentikan.")
        client.close()
        running = False
        break

    if pesan_user == "machine":
        res = platform.machine()
        client.send(res.encode())
    elif pesan_user == "system":
        res = platform.system()
        client.send(res.encode())
    elif pesan_user == "release":
        res = platform.release()
        client.send(res.encode()) 
    elif pesan_user == "version":
        res = platform.version()
        client.send(res.encode())
    elif pesan_user == "node":
        res = platform.node()
        client.send(res.encode())
    else:
        client.send(b"Perintah tidak dikenal")

    client.close()

server.close()
print("Server OFF.")
