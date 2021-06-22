from random import random
def ast():
    while True:
        cmd = input("*> ")
        if cmd == "*": print("Hello World")
        elif cmd == " * ": print(random() * 2147483647)
        elif cmd == "**": print("Who can say where the road goes"), print("Where the day flows, only time"), print("And who can say if your love grows"), print("As your heart chose, only time")

        elif cmd == "*+*":
            while True: pass
            while False: print("Even a million scars doesn't change whose you are"), print("You're worthy"), print("Beautifully broken")
File_object = open(r"example.txt","r")