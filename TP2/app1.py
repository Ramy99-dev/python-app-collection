number = int(input("Donner un nombre : "))

inf = int(input("Donner la borne inferieure : "))
sup = int(input("Donner la borne superieure : "))

if(inf > sup):
    print("Erreur ! La borne inferieure doit etre < borne superieure .")
else:
    if(sup > number > inf ):
        print("number appartient a [{0},{1}] ".format(inf,sup))
    else:
        print("number n'appartient pas a [{0},{1}] ".format(inf,sup))