'''
pvt and public ip address important to understand

sockets: (are communication endpoints - one talks to the other)
internet
operating system
bluetooth socket

#socket examples
Socket.AF_INET #an internet socket ipv4
Socket.AF_BLUETOOTH #bluetooth socket
Socket.AF_INET6 # ipv6

#is it of type:
#TCP is connection based, reliable, can detect packet loss, confirmation, terminates on command.
SOCK_STREAM #tcp - transmission control protocaol - establishes an egreement of open exchange

#UDP - If it gets lost it's lost, you dont know. No gauranteed order of messages.
#It's advantage is that it's more realtime - faster, less network and pc stress.
SOCK_DGRAM #UDP - user datagram protcoal - A sends to B, done. B sends to A, done.
'''

#This example handles one connection using SOCK_STREAM. Use multithreading for multiple connections.
import socket

#get my ip address
HOST = socket.gethostbyname(socket.gethostname())
# use manual ip input if working on virtualbox 127.0.0.1 also works
#HOST = '192.168.0.111'
PORT = 9090

#HOSTING SOCKET:
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
#listen for connections and optionally limit the waiting connections
server.listen()

#CLIENT CONNECTION SOCKET:
#this socket just waits for incoming connections
#endless loop
while True:
    #communication_socket returned by the accept method
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
                                             # the bytes must be encoded utf-8 e.g
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is {message}")
    communication_socket.send("Got your message thank you!".encode('utf-8'))
    communication_socket.close()
    print(f"connection with {address} ended!".encode('utf-8'))
