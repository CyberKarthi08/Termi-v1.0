import os
import threading
from time import sleep
import ipaddress
import math


def set_thread(name):
    print("Function Started & Going On....")
    print("Let's Wait 2 Sec & You Get a Terminal Access...")
    sleep(0.5)
    Terminal = input("$")
    os.system(Terminal)

    print("The Function Thread End By....\n", name)



if __name__ == "__main__":

    print(f"\nThe Main Started By....")
    user = input("Who Are You : ")

    set_thread("Normal Function")

    var_thread = list()
    print("Let's Wait 2 Sec...Thread Will Be Starting....\n")
    sleep(2)
    while True:
        print("Thread Going On Let's Wait 2 Sec...")
        demo = threading.Thread(target=set_thread(user), args=(1,))
        demo.start()
        # demo.join()
        var_thread.append(demo)
        sleep(2)



print("Finally The Main Ended.....")
