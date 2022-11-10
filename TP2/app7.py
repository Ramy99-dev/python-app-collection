a = int(input("Donner a : "))
b = int(input("Donner b : "))

def calculPGCD(a ,b):
    if(a == b):
        return a
    else:
        if a > b :
            return calculPGCD(a-b , a)
        else:
            return calculPGCD(a ,b-a)


print("PGCD({0},{1}) = {2}".format(a,b,calculPGCD(a,b)))
