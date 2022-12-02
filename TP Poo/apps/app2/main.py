from biblio import *
from livre import *
from abonne import *


b = Bibiotheque()
l1 = Livre("Titre 1" , 3)
b.ajouter_livre(l1)
a1 = Abonne("112121212","Rami",False,0)
b.ajouter_abonne(a1)
print(b.emprunteurs)
print(b.livres)
print(b.livres[l1.num])
b.emprunter(a1.getNcin(),l1.num)
print(b.livres[l1.num])
print(b.operations)
