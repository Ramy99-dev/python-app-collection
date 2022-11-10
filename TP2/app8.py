a = float(input("Donner a : "))
b = float(input("Donner b : "))
c = float(input("Donner c :"))

if a > b and a > c :
    a,c = c,a 

elif b > a and b > c :
    b,c = c,b

if a + b >= c :
    print("Les longueurs correspondent à un triangle")
elif a**2 + b**2  == c**2:
    print("Le triangle est rectangle")
    if a == b :
        print("Le triangle est isocèle et rectangle")
elif (a == b) == c :
    print("Le triangle est équilatérale")

