import socket
import threading
import time
import os
import ipaddress
import math

SERVER_IPADDR = "192.168.58.254"
PORT = 5449
MEMBER_DETAILS = {}

class Server_Connection_Process:

    # If you have store a user's names
   

    def __init__(self, server_sock=None):
            if server_sock is True:
                self.server_sock = server_sock 

    def server_connection_binding(self):
        self.server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server_sock.bind((SERVER_IPADDR, PORT)) 
    def server_listening_process(self):
        self.server_sock.listen(0)
        print(f"Listening on {SERVER_IPADDR}:{PORT}")
        client_recv_data, client_connection_data = self.server_sock.accept()
        with client_recv_data:
            print(f"Connection Established By {client_connection_data[0]}:{client_connection_data[1]}")
            while True:
                recv_data = client_recv_data.recv(1024)
                self.server_sock.sendall("[+] Configure your hostname : ")
                recv_data = recv_data.decode('utf-8')
                if recv_data == "close":
                     client_recv_data.send("closed".encode("utf-8"))
                     break
                print(f"Data: {recv_data}")
                client_recv_data.sendall(recv_data)
                    
           

if __name__ == "__main__":
    main_thread = Server_Connection_Process()
    main_thread.server_connection_binding()
    main_thread.server_listening_process()

    
            


# def termi_interface(self=True):
            



#         self.user_name = str(input("Who are you : "))
#         print(f"Hey, Hi {self.user_name} Welcome to visit our service", end="!!!")
#         main_thread = threading.Thread(target=main_Termin.termi_interface, args=(self,),daemon=False)

#         print("\nIf you access our Termi-Infrastructure\n")
#         terminal_access_input = input(" yes  ||  no : \n\n")
#         if terminal_access_input == 'yes':
#             print("Wait 2 sec to connecting\n")
#             time.sleep(2)
#             while True:
#                 command = input("$ ")
#                 os.system(command)
#                 if command == 'exit':
#                     print(f"{user} connection quited\n")

#                     break
#         elif terminal_access_input == 'no':
#             print("Okay...Let Move Forward ")
#         else:
#             print("Error : Type valid input ")

#         main_thread.start()
#         def get_user_name(self):
#             print(user_name)

# # demo = main_Termin()
# main_Termin.termi_interface()








