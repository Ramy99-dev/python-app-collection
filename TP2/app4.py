moyenne = float(input("Donner la moyenne : "))

while moyenne < 0 and moyenne > 20:
    moyenne = float(input("Donner la moyenne : "))

if moyenne >= 16:
    print("Tres bien")
elif moyenne >= 14:
    print("Bien")
elif moyenne >= 12:
    print("Assez Bien")
else:
    print("Passable")
