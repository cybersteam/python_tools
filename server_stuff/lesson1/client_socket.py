# use https://myip.is/ to get public ip's
import socket

HOST = socket.gethostbyname(socket.gethostname())
#HOST = "165.0.96.165"
PORT = 9090

#SERVER TALK SOCKET
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send(f"hello world".encode('utf-8'))
#number of bytes specified here.
print(socket.recv(1024))
