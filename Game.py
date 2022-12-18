import random
import numpy as np
import sys
from Level1 import level1

print("Привет, друг! Ты попал в мини-игру \"Отгадай энергетик\".")

while(True):
    
    answer1 = input("Желаешь испытать свои знания в энергетиках?: ")
    
    if answer1 == "да":
        break
    elif answer1 == "нет":
        sys.exit()
    elif answer1 == "стоп":
        sys.exit() 
    else:
        continue

level1()

print("""Поздравляю! Ты прошёл 1 уровень!""")

while(True): 
    
    level1answer = input("""Хочешь продолжить? """)
               
    if level1answer == "да":
        print("Ожидайте продолжения...")
        break
    elif level1answer == "нет":
        sys.exit()
    elif level1answer == "стоп":
        sys.exit()
    else:
        continue
