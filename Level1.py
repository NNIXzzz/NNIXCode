def level1():
    import random
    import numpy as np
    import sys
    
    Scores = 0
    Three = 3
    diceE = ["adrenaline", "tornado", "burn", "eon", "redbull", "doubleyou", "drive", "gorilla"]

    while Scores < 15:
        
        RDE = random.choice(diceE)
        diceE.remove(RDE)     
        RDE1 = RDE
        RDE1 = RDE1.replace(random.choice(RDE1), '*')
        print(RDE1, end=' - ')

        answerdiceE = input()
        if answerdiceE == RDE:
            Scores = Scores + Three
            print("Отгадал!", end=" ")
            print(("Баллы:"),(Scores),"""
                """, sep="")
    
        if answerdiceE == "стоп":
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