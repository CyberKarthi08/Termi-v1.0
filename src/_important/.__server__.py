import socket
import threading
import subprocess
from time import sleep
import codecs
import os
import sys
import ipaddress
import math

SERVER_IPADDR = "192.168.152.254"
PORT = 5449
MEMBER_DETAILS = []

class Server_Connection_Process(threading.Thread):

    # If you have store a user's names
   

    def __init__(self, server_sock=None,client_send_data=None,server_recv_data=None,client_connection_data=None,send_message=None):
                self.server_sock = server_sock 
                self.send_message = send_message
                self.client_send_data = client_send_data
                self.server_recv_data = server_recv_data
                self.client_connection_data = client_connection_data

    def server_binding_process(self):
            self.server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_sock.bind((SERVER_IPADDR, PORT))

    def server_connecting_process(self):
        with self.server_sock:
            self.server_sock.listen(0)
            print(f"[+] Listening on {SERVER_IPADDR}:{PORT}")
            while self.server_sock.listen:
                self.client_send_data, self.client_connection_data = self.server_sock.accept()
                print("[+]",self.client_send_data)
                print("[-]",self.client_connection_data)
                Server_Connection_Process.Initial_send_messages(self)
                Server_Connection_Process.server_recv_meassage(self,recv_data=self.client_send_data)
                # self.server_recv_data = self.client_send_data.recv(1024).decode('utf-8')
                # MEMBER_DETAILS.append(self.server_recv_data)
                print(f"[+] Connection Established By @_{MEMBER_DETAILS[0]} {self.client_connection_data[0]}:{self.client_connection_data[1]}")

                Server_Connection_Process.server_send_data(self,send_message=f"@{MEMBER_DETAILS[0]}, Would you like to access our server infrastructure?")
                Server_Connection_Process.server_recv_meassage(self,recv_data=self.client_send_data)
                print(MEMBER_DETAILS)
                if MEMBER_DETAILS[1] == "Yes":
                    while True:
                        Server_Connection_Process.server_access_permission(self)
                        # if MEMBER_DETAILS[2] is True:
                        #     recv_data = self.client_send_data.recv(1024).decode('utf-8')
                        #     MEMBER_DETAILS.append(recv_data)
                        #     print(MEMBER_DETAILS[3])
                    # task_thread = threading.Thread(target=self.server_access_permission(),args=(self,))
                    # task_thread.daemon = False # This ensures the thread will exit when the main program exits
                    # task_thread.start() 
                else:
                    request_acess_permission = f"{self.server_recv_data}, If your Connection lost".encode(encoding='UTF-8',errors='strict')
                    self.client_send_data.send(request_acess_permission)  
                
                
    def server_access_permission(self):
        while True:
            print(MEMBER_DETAILS[1])
            Server_Connection_Process.server_send_data(self,send_message=f"Termi_Server@{MEMBER_DETAILS[0]}:~$ ")
            self.server_recv_data = self.client_send_data.recv(1024).decode('utf-8')
            # MEMBER_DETAILS.append(self.server_recv_data) 
            # Server_Connection_Process.server_recv_meassage(self,recv_data=self.client_send_data)
                    # MEMBER_DETAILS= self.server_recv_data
            # print("[+]",MEMBER_DETAILS[2])
            try:
                termi_command_result= subprocess.run(self.server_recv_data, shell=True, capture_output=True, text=True)
                print(termi_command_result)
                print(type(termi_command_result))
                output = termi_command_result.stdout + termi_command_result.stderr  # Capture both stdout and stderr
            except Exception as e:
                output = str(e)

                        # Send the command output back to the client
            self.client_send_data.send(output.encode('utf-8'))
                    # promt_result = [os.system(MEMBER_DETAILS[2])]
                    # print(type(promt_result))
                    # print(promt_result)
                    # promt_result = codecs.encode(promt_result[0], 'utf-8')
                    # self.client_send_data.send(promt_result)
                    # return promt_result
    
            

    def Initial_send_messages(self):
        __Initial_message = ["Hey...Hi...👋\nWe welcome you to check out our service 🎉...\nConfigure your hostname\n"]
        encoded_messages = [message.encode('utf-8') for message in __Initial_message]
        for encoded_message in encoded_messages:
            self.client_send_data.send(encoded_message)

    def server_send_data(self,send_message):
        send_message = codecs.encode(send_message, 'utf-8')
        self.client_send_data.send(send_message)

    def server_recv_meassage(self,recv_data):
        recv_data = self.client_send_data.recv(1024).decode('utf-8')
        MEMBER_DETAILS.append(recv_data)
        
         
          

         
         
        
                    
           

if __name__ == "__main__":
    main_thread = Server_Connection_Process()
    main_thread.server_binding_process()
    main_thread.server_connecting_process()