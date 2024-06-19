import time
import os
import threading

class main_Termin:

    # If you have store a user's names


    def __init__(self=True, user_name = None):
        print('''
        ________________ _______ ________________
        \__   __(  ____ (  ____ |       )__   __/
            ) (  | (    \/ (    )| () () |  ) (
            | |  | (__   | (____)| || || |  | |
            | |  |  __)  |     __) |(_)| |  | |
            | |  | (     | (\ (  | |   | |  | |
            | |  | (____/\ ) \ \_| )   ( |__) (___
            )_(  (_______//   \__//    \\\_______/  v1.0
            ''')
        self.user_name = user_name



    def termi_interface(self=True):
        self.user_name = str(input("Who are you : "))
        print(f"Hey, Hi {self.user_name} Welcome to visit our service", end="!!!")
        main_thread = threading.Thread(target=main_Termin.termi_interface, args=(self,),daemon=False)

        print("\nIf you access our Termi-Infrastructure\n")
        terminal_access_input = input(" yes  ||  no : \n\n")
        if terminal_access_input == 'yes':
            print("Wait 2 sec to connecting\n")
            time.sleep(2)
            while True:
                command = input("$ ")
                os.system(command)
                if command == 'exit':
                    print(f"{user} connection quited\n")

                    break
        elif terminal_access_input == 'no':
            print("Okay...Let Move Forward ")
        else:
            print("Error : Type valid input ")

        main_thread.start()
        def get_user_name(self):
            print(user_name)

# demo = main_Termin()
main_Termin.termi_interface()








