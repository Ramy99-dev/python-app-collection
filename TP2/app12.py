number = int(input("Donner un nombre : "))

def withForLoop(number):
    fact = 1
    if number != 0:
        for i in range (1,number+1):
            fact *= i
    return fact

def withWhileLoop(number):
    fact = 1
    if number != 0:
        i = 1
        while i < number+1:
            fact *= i
            i+=1
    return fact

print("{0}! = {1}".format(number,withForLoop(number))) 
print("{0}! = {1}".format(number,withWhileLoop(number))) 