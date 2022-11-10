a = int(input("Donner a :"))
b = int(input("Donenr b :"))

prod = 0
for i in range(0,b):
    prod += a

print("{0} * {1} = {2}".format(a,b,prod))
