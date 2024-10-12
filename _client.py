import re
import socket
from time import sleep

SERVER_IPADDR = '192.168.152.254'
PORT = 5449

__LIST__ = ["Configure your hostname", "Yes | No" ]

CLIENT_DATA = []

class Client_Connection_Process:
	def __init__(self,client_sock=None, client_send_message=None,client_recv_msessage=None):
		self.client_sock = client_sock
		self.client_send_message = client_send_message
		self.client_recv_message = client_recv_msessage

	def client_connecting_process(self):
		self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF - Address Family , #INET - Internet
		self.client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)		
		self.client_sock.connect((SERVER_IPADDR,PORT))
		print(f"\n[+] Connection Established By {SERVER_IPADDR}:{PORT}\n")
		# while True:
		with self.client_sock:
			self.client_recv_message = [self.client_sock.recv(1024).decode('utf-8')]
			initial_message = self.client_recv_message[0].splitlines()
			for message in initial_message:
				sleep(1.5)
				print(f"[+] {message}\n")
				# if initial_message is True:
				# 	Client_Connection_Process.send_message()
			self.client_send_message = input("[*] HOST_Name  @_")
			self.client_sock.send(self.client_send_message.encode(encoding='UTF-8',errors='strict'))
			# self.client_recv_message = self.client_sock.recv(1024).decode('utf-8')
			# print(f"[+] {self.client_recv_message}")
			Client_Connection_Process.rec_message(self)
			try:
				self.client_send_message = input("\n[Yes/No]")
				self.client_sock.send(self.client_send_message.encode('utf-8')) 
				
				self.client_recv_message = self.client_sock.recv(1024).decode('utf-8')
				print(f"\n{self.client_recv_message}",end="")
				self.client_send_message = input()
				self.client_sock.send(self.client_send_message.encode('utf-8'))
				Client_Connection_Process.rec_message(self)
					
			except self.client_sock.timeout:
				print("Error")
				self.client_recv_message = self.client_recv_message[0].splitlines()
				print(f"\n[+] {self.client_recv_message[0]}")
				if(self.client_send_message == "quit"):
					self.client_sock.close

	def send_message(self):
			self.client_send_message = input()
			if(self.client_send_message == "quit"):
				self.client_sock.close
			# message = name + ": " + msg
			self.client_sock.sendall(self.client_send_message.encode('utf-8'))

	def rec_message(self):
		self.client_recv_message = self.client_sock.recv(1024).decode('utf-8')
		print(f"\n[+] {self.client_recv_message}")


if __name__ == "__main__":

	main_client = Client_Connection_Process()
	main_client.client_connecting_process()
	# main_client.send_recv_message_manage()		

