import os
import time
import pyautogui as pg

logo = """
 _    _      _                            _____                                           
| |  | |    | |                          /  ___|                                          
| |  | | ___| | ___ ___  _ __ ___   ___  \ `--. _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \  `--. \ '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
\  /\  /  __/ | (_| (_) | | | | | |  __/ /\__/ / |_) | (_| | | | | | | | | | | |  __/ |   
 \/  \/ \___|_|\___\___/|_| |_| |_|\___| \____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                               | |                                        
                                               |_|                                                                      

Created by @h.awtsauce
                """
logo2 = """
 _____                                 _             
/  ___|                               (_)            
\ `--. _ __   __ _ _ __ ___  _ __ ___  _ _ __   __ _ 
 `--. \ '_ \ / _` | '_ ` _ \| '_ ` _ \| | '_ \ / _` |
/\__/ / |_) | (_| | | | | | | | | | | | | | | | (_| |
\____/| .__/ \__,_|_| |_| |_|_| |_| |_|_|_| |_|\__, |
      | |                                       __/ |
      |_|                                      |___/ 
"""

os.system("cls")
os.system("color a")

print(logo)
message = input("Type the word/phrase to be spammed: ")
os.system("cls")
print("Spam Started in 3 Seconds.")
time.sleep(3)
os.system("cls")
print(logo2)
print("İf You Want The Stop Press CTRL-C")
os.system("curl parrot.live")
def spam():
    pg.typewrite(message)
    pg.press("enter")

while True:
    spam()