#scannning ports
import socket
from IPy import IP

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        sock.settimeout(0.5) #scans ports faster but can lose accuracy
        print(str(port) + " is open")
    except:
        pass
        #print(str(port) + " is closed")

ipaddress = input('enter the ip: ')
converted_ip = check_ip(ipaddress)

for port in range (1,100):
    scan_port(converted_ip, port)
