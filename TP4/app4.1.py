l = []

listSize = int(input("Donner le nombre des élements : "))

while 50<listSize<6:
    listSize = int(input("Donner le nombre des élements : "))

for  i in range (0 , listSize):
    l.append(int(input("Donner un entier : ")))

r = []
somme = 0
for  i in range (0 , listSize):
    somme += l[i]
    r.append(somme)

print(l)
print(r)
