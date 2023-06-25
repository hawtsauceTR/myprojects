import pyautogui as pg
import time
import os

os.system("color a")
os.system("cls")


text = input("Ne Yazılsın?: ")
title = input("Başlık Ne Olsun?: ")
button = input("Buttona Ne Yazılsın?: ")


os.system("cls")
time.sleep(3)
print("Oluşturuluyor...")
time.sleep(2)
os.system("cls")


pg.alert(text=text, title=title, button=button)
time.sleep(1)

wannasee=input("Kodun Nasıl Yazıldığını Görmek İster misin?(y/n): ")
if wannasee == "y":
    print("alert(text='Buraya metin', title='Başlık', button='OK')")
else:
    os.system("exit")