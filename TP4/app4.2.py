n = float(input("Donner un reel : "))
n = str(n)

pos = n.find('.')

n = n[pos+1:]
print(n)

l = []

for i in n :
    l.append(int(i))
print(l)

