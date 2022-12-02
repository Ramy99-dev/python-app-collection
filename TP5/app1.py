import random 

list = []
def listAleaInt(n ,a , b):
    for i in range (0,n):
        list.append(random.randint(a,b))
    
listAleaInt(int(input("Donner la taille du tableau : " )),
            int(input("Donner la valeur min : ")),
            int(input("Donner la valeur max : ")))

minValIndex = list.index(min(list))

print(list)

print(minValIndex)

list[0] , list[minValIndex] = list[minValIndex] , list[0]

print(list)

    