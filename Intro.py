import sys
from Game import start

def intro():
    
    print("Привет, друг! Ты попал в мини-игру \"Отгадай энергетик\".")
    answer1 = input("Желаешь испытать свои знания в энергетиках?: ")
    answer1 == "да"
    if answer1 == "да":
            start()
    elif answer1 == "нет":
            sys.exit()
intro()