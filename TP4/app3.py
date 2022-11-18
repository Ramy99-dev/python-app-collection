l = []

listSize = int(input("Donner le nombre des élements : "))

for  i in range (0 , listSize):
    l.append(int(input("Donner un entier : ")))

maximum = l[0]
minimum = l[0]
somme = 0 

for i in range(1 , listSize):
    if(l[i] > maximum):
        maximum = l[i]

for i in range(1 , listSize):
    if(l[i] < minimum):
        minimum = l[i]

for i in range(0 , listSize):
    somme += l[i]

print(maximum)
print(minimum)
print(somme)