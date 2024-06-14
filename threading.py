from time import sleep
import os


class Main_Threading:
    def __init__(self,user):
        print(f"\nHey, Hi {user} Welcome! To visit our service",)

    def user1(self,command):
        print("let's open our terminal access ")
        in_put = self
        if in_put == "Y":
            command = list()
            os.system(command)



calling = Main_Threading(input("who are you : "))

calling1 = Main_Threading.user1(input("$ "))





