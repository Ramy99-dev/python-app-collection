number = int(input("Donner un entier : "))
isPrimary = True

for i in range(2 , number/2):
    if(number % i == 0):
        isPrimary = False
        
if isPrimary : 
    print("{0} est un nombre premier".format(number))
else:
    print("{0} n'est pas un nombre premier".format(number))
