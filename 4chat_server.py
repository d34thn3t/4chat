import sys
import _thread
import socket
from time import sleep

global s

global buf

buf=""

global exitcode

exitcode=0

global f

f=open('srv.log','a')

def saccept():

	global exitcode

	while exitcode!=1:

		c,addr=s.accept()

		f.write(str(addr))

		_thread.start_new_thread(connhandle,(c,addr))

def decd(txt):

	return txt.decode("utf-8")

def encd(txt):

	return str.encode(txt)

def connhandle(cli,adr):

	global exitcode

	uid=decd(cli.recv(1024))

	cli.send(encd("HI!"))

	global buf

	rec=''

	while True:

		rec=cli.recv(1024)

		buf+=uid+"> "+decd(rec)+'\n'

		if(decd(rec)=='exit'):

			break

		cli.send(encd(buf))

		if exitcode==1:

			cli.send(encd("EXIT"))

			cli.recv(1024)

			break

	cli.close()

if(len(sys.argv)!=3):

	print("USAGE: "+sys.argv[0]+" <ip> <port>")

	exit()

try:

	global host

	global port

	global s

	host=sys.argv[1]

	port=int(sys.argv[2])

	s=socket.socket()

	print("BINDING TO "+host+':'+str(port))

	s.bind((host,port))

	s.listen(5)	

except socket.error as msg:

	print(str(msg))

_thread.start_new_thread(saccept,())

while exitcode!=1:

	exitcode=int(input("Type 1 to exit:"))

	sleep(10)

	print("EXITED!")

s.close()

f.close()



	

	

	



