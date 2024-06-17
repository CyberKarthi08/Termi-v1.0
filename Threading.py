import time
import os
import threading


class main_Termin:
    def termi_interface(self=None, users=None):
        print(''' \t\t
________________ _______ ________________
\__   __(  ____ (  ____ |       )__   __/
   ) (  | (    \/ (    )| () () |  ) (   
   | |  | (__   | (____)| || || |  | |   
   | |  |  __)  |     __) |(_)| |  | |   
   | |  | (     | (\ (  | |   | |  | |   
   | |  | (____/\ ) \ \_| )   ( |__) (___
   )_(  (_______//   \__//    \\\_______/  v1.0
''')
        main_thread = threading.Thread(target=main_Termin.termi_interface, args=users, daemon=True)
        users = input("Who are you : ")
        print(f"Hey, Hi {users} Welcome to visit our service\n", end="!!!")
        print("If you access our Termi-Infrastructure\n")
        users = input(" yes  ||  no : \n\n")
        if users == 'yes':
            print("Wait 2 sec to connecting\n")
            time.sleep(2)
            while True:
                command = input("$ ")
                os.system(command)
                if command == 'exit':
                    break

        elif users == 'no':
            print("Okay...Let Move Forward ")
        else:
            print("Error : Type valid input ")

        main_thread.start()


termi_interface1 = threading.setprofile(main_Termin.termi_interface(main_Termin))

termi_interface1.start()

termi_interface1.run()



