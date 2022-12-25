def level1():
    import random
    import numpy as np
    import sys
    import string
    
    Scores = 0
    Three = 3
    Half = 1/2
    
    diceE = ["Adrenaline", "Tornado", "Burn", "Eon", "Redbull", "Doubleyou", "Drive", "Gorilla"]

    while Scores < 15:
        
        RDE = (random.choice(diceE))
        RDEScore = (Half*len(RDE))
        diceE.remove(RDE)     
        RDE1 = RDE
        RDE1 = RDE1.replace(random.choice(RDE1), '*')
        print(RDE1, end=' - ')

        answerdiceE = input()
        answerdiceE = answerdiceE.capitalize()
        if answerdiceE == RDE:
            Scores = Scores + RDEScore
            print("Отгадал!", end=" ")
            print(("Баллы: "),(Scores),"""
                """, sep="")
    
        if answerdiceE == "Стоп":
            sys.exit()
        elif answerdiceE != RDE:
            Scores = np.subtract(Scores, Three)
            print("Неудача!", end=" ")
            print(("Баллы:"),(Scores),"""
                """, sep="")
        
        if diceE == []:
            print("""Баллы закончились, попробуй ещё раз!""")
            diceE = ["adrenaline", "tornado", "burn", "eon", "redbull", "doubleyou", "drive", "gorilla"]
            Scores = 0
            continue