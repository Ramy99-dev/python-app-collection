max = int(input("Donner la valeur maximale : "))

somme = 0 
produit = 1

for i in range(1,max):
    if i % 5 != 0 :
        somme += 1/i
        produit *= 1/i


print(somme)
print(produit)