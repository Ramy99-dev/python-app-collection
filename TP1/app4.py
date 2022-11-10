a = int(input("a = "))
b = int(input("b = "))

while a < 0 or b < 0 :
    a = int(input("a = "))
    b = int(input("b = "))  

q = a // b
r = a % b

print("{0} = {1} * {2} + {3} ".format(a,b,q,r))