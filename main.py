import threading
from time import sleep


def set_thread(name):
    print("Function Thread Started & Going On....")
    sleep(0.5)
    print(f"The Function Thread End.....End {name}")

if __name__ == "__main__":

    print("The Main Started......By", input("Who Are You : "))
    set_thread("That Function")
    demo = threading.Thread(target=set_thread, args=("HAcker",), daemon=True)
    print("Let's Wait 5 Sec...Thread Will Be  Starting....", sleep(5))
    demo.start()
    print("Finally The Main Function Ended.....")
