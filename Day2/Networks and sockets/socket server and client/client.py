#Socket client - client.py

import socket

HOST = "127.0.0.1" #server host
PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

message = "Hi server"
print("Client: " + message)
client_socket.send(message.encode("utf-8"))

data_from_server = client_socket.recv(1024)
print("Server: " + data_from_server.decode("utf-8"))

while True:
    data_from_server = client_socket.recv(1024)
    print("Server: " + data_from_server.decode("utf-8"))

    if data_from_server == "exit":
        break

    client_chat = input()
    print("Client: " + client_chat)
    client_socket.send(client_chat.encode("utf-8"))

client_socket.close()