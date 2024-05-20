import socket
import sys
MAX_PKT_LEN = 1024
PORT_NUM = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ('10.186.1.157', PORT_NUM)
s.bind(server)

while True:
    data, address = s.recvfrom(MAX_PKT_LEN)
    print(address)
    clientMsg = "Message from Client:{}".format(data.decode('ascii'))
    print(clientMsg)
    s.sendto(data, address)
