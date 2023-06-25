import random 
import os
import time

logo = """
  ________                               _______               ___.                        
 /  _____/ __ __   ____   ______ ______  \      \  __ __  _____\_ |__   ___________  ______
/   \  ___|  |  \_/ __ \ /  ___//  ___/  /   |   \|  |  \/     \| __ \_/ __ \_  __ \/  ___/
\    \_\  \  |  /\  ___/ \___ \ \___ \  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/\___ \ 
 \______  /____/  \___  >____  >____  > \____|__  /____/|__|_|  /___  /\___  >__|  /____  >
        \/            \/     \/     \/          \/            \/    \/     \/           \/ 

Created by @h.awtsauce
                                                                       
       """
os.system("color a")
os.system("cls")
print(logo)
chance = 3

number = random.randint(1,10)

while True:
    guessnumber = int(input("1 İle 10 Arasında Bir Sayı Tahmin Ediniz: "))

    if guessnumber != number:
        os.system("cls")
        chance -= 1
        print("Yanlış,",chance,"Hakkınız Kaldı,Tekrar Deneyin: ")

    else:
        os.system
        print("Tebrikler,Kazandınız")
        break

    if chance == 0:
        print("Üzgünüm Bütün Hakkınız Bitti,Kaybettiniz.")
        break
