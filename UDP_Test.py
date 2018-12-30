# -*- coding: utf-8 -*-
import socket

i = 1

#while (i == 1):
UDP_IP = "192.168.100.77"
UDP_PORT = 1234
MESSAGE = "Test=245.7"

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind( ("",4321) )

datareturn, addr = sock2.recvfrom(1024)
print datareturn

if MESSAGE == datareturn:
    xSendenOk = 1
    print ("RFID Chip gelesen und von Loxone bestaetigt!")
