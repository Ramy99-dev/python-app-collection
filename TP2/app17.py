import random
import os
import time


def loading():
    animation = [
    "[        ]",
    "[=       ]",
    "[===     ]",
    "[====    ]",
    "[=====   ]",
    "[======  ]",
    "[======= ]",
    "[========]",
    "[ =======]",
    "[  ======]",
    "[   =====]",
    "[    ====]",
    "[     ===]",
    "[      ==]",
    "[       =]",
    "[        ]",
    "[        ]"
    ]

    notcomplete = True

    i = 0

    while notcomplete:
        print(animation[i % len(animation)].center(140))
        time.sleep(.1)
        i += 1
        if i == 20:
            break

def gameName():
    print('''

  ________                                ________                       
 /  _____/ __ __   ____   ______ ______  /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/ /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \ \  \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >  \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/          \/     \/      \/     \/ 
    

'''
)


def chooseNumber(randomNumber):
    playerNumber = int(input("Donner un nombre [0-100] : "))
    checkNumber(randomNumber , playerNumber)

def startGame(choice):
    if(choice == 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        gameName()
        randomNumber = random.randint(0, 100)
        chooseNumber(randomNumber)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Aurevoir")
        exit()

def checkNumber(randomNumber , playerNumber):
    if(playerNumber == randomNumber):
         os.system('cls' if os.name == 'nt' else 'clear')
         gameName()
         print("Tu gagnier , Bravo !")
         print("1 - Rejouer  ")
         print("0 - Sortir ")
         choice = int(input("Choix : "))
         os.system('cls' if os.name == 'nt' else 'clear')
         loading()
         startGame(choice)
    else:
       if(randomNumber > playerNumber):
            print("Plus Grand")
       else:
            print("Plus Petit")
       chooseNumber(randomNumber)
        

os.system('cls' if os.name == 'nt' else 'clear')
loading()
os.system('cls' if os.name == 'nt' else 'clear')
gameName()
print("1 - Commencer le jeu  ")
print("0 - Sortir ")
choice = int(input("Choix : "))
startGame(choice)




