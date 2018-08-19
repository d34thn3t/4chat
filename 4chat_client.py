import sys
import os
import socket

def decd(txt):

	return txt.decode("utf-8")

def encd(txt):

	return str.encode(txt)

def clearscreen():

	if os.name=='nt':

		os.system("cls")

	else:

		os.system("clear")

if(len(sys.argv)!=4):

	print("USAGE: "+sys.argv[0]+" <username> <ip> <port>")

	exit()

s=socket.socket()

s.connect((socket.gethostbyname(sys.argv[2]),int(sys.argv[3])))

s.send(encd(sys.argv[1]))

while True:

	buf=decd(s.recv(10240))

	if buf=="EXIT":

		s.send("EXITED!")

		break

	clearscreen()

	print(buf)

	inp=input(sys.argv[1]+">")

	s.send(encd(inp))

s.close()




