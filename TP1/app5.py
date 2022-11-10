n = int(input("Donner nombre d'article : "))

TVA = 0.196
prixHT = float(input("Donner prix HT : "))
print("Nombre d'article : {0} ".format(n))
print("prix HT : {0} DT".format(prixHT))
prixTTC = 0
for i in range(0,n):
    prixTTC += prixHT+(prixHT * TVA)
print("prix TTC : {0} DT".format(prixTTC))