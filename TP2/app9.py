number = int(input("Donner un entier : "))
while number < 0 :
    number = int(input("Donner un entier : "))
isPerfect = False

divList = []

for i in range(1,number/2 + 1):
    if(number % i == 0):
        divList.append(i)

print(divList)
somme = 0

for i in divList:
    somme += i

if somme == number :
    print("{0} est nombre parfait".format(number))