import socket

HOST = '127.0.0.1'
PORT = 5443

name = input("Enter your name: ");

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					#AF - Address Family
					#INET - Internet
					
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((HOST, PORT))
print(s.recv(2048).decode())
while(True):
	msg = input("Message: ")
	if(msg == "quit"):
		break
	msg = name + ": " + msg
	s.sendall(msg.encode())
s.close()
