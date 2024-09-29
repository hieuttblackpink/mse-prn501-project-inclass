import socket

HOST = "127.0.0.1" #server host
PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

file = open("/Users/hieutt/MSE - FPT/Fall 2024/PPR501/Project/In-class/Day2/Networks and sockets/Excercise/Excercise 3/text.txt")
data = file.read()
client_socket.send(str(data).encode())
file.close()

client_socket.close()