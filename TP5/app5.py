def valide(adn):
    valid = False
    for i in adn :
        if (i not in('atgc') ):
            break
    if(adn.index(i) == len(adn)-1):
        valid = True
    if(valid):
        print("La sequence est valide")
    else:
        print("La sequence est invalide")

def saisie():
    adn = input("Donner la sequence d'adn : ")
    valide(adn)
    print(adn)

def proportion(str , seq):
    return str.count(seq)

adn = ""
saisie()
