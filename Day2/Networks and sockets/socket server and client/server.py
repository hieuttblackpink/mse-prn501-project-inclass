# Socket server - server.py

import socket

HOST = "127.0.0.1" #local host
PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("Connecting...")

connect, address = server_socket.accept()

recieve_data_from_client = connect.recv(1024)
print("Client: " + recieve_data_from_client.decode("utf-8"))

message = "Hi client"
print("Server: " + message)
connect.send(message.encode("utf-8"))

while True:
    server_chat = input()
    print("Server: " + server_chat)

    if server_chat == "exit":
        break

    connect.send(server_chat.encode("utf-8"))
    recieve_data_from_client = connect.recv(1024)
    print("Client: " + recieve_data_from_client.decode("utf-8"))

connect.close()

