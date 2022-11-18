n = int(input("Donner la taille de la matrice : "))

mat1 = []
mat2 = []

print("Remplissage matrice 1 : ")

for i in range (0,n):
    l1 = []
    for j in range(0,n):
        l1.append(int(input("Donner un entier : ")))
    mat1.append(l1)

print("Remplissage matrice 2 : ")

for i in range (0,n):
    l2 = []
    for j in range(0,n):
        l2.append(int(input("Donner un entier : ")))
    mat2.append(l2)


print(mat1)
print(mat2)


somme = []

for i in range(0,n):
    sommeList = []
    for j in range(0,n):
        sommeList.append((mat1[i][j]+mat2[i][j]))
    somme.append(sommeList)

substraction = []

for i in range(0,n):
    subList = []
    for j in range(0,n):
        subList.append((mat1[i][j]-mat2[i][j]))
    substraction.append(subList)


etc = []
for i in range(0,n):
    etcList = []
    for j in range(0,n):
        etcList.append((3*mat1[i][j]+10*mat2[i][j]))
    etc.append(etcList)

print("Somme : ")
print(somme)

print("Substraction : ")
print(substraction)


print("3A + 10*B : ")
print(etc)

