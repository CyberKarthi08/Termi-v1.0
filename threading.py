import time
import os
import threading

class main_threading1:
    def join_users():
        print(""" 

_________ _______  _______  _______ _________                            
\__   __/(  ____ \(  ____ )(       )\__   __/                            
   ) (   | (    \/| (    )|| () () |   ) (                               
   | |   | (__    | (____)|| || || |   | |                               
   | |   |  __)   |     __)| |(_)| |   | |                               
   | |   | (      | (\ (   | |   | |   | |                               
   | |   | (____/\| ) \ \__| )   ( |___) (___                            
   )_(   (_______/|/   \__/|/     \|\_______/                       __   
                                          ( \        |\     /|     /  \  
                                           \ \       | )   ( |     \/) ) 
                                            \ \      | |   | | _____ | | 
                                             ) )     ( (   ) )(_____)| | 
                                             / /       \ \_/ /        | | 
                                           / /         \   /       __) (_
                                          (_/_____      \_/        \____/
                                            (_____)                      

            """)
        users = list()
        name_1 = input("Who are you : \n")
        print(f"Hey, Hi {name_1} Welcome to visit our service!!!\n")
        users.append(name_1)
        print(users)

    def termin_access(self,access):
        print("If you access our 'Termin' Window \n")
        okk = threading.Thread()
        access1=input("Y or N : ")
        if access1 == 'Y' | 'N':
            print("Okay")
            os.system(access1)
        else:
            print("Issus")


main_threading1.join_users()
main_threading1.termin_access(access)
