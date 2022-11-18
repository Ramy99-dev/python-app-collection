tuple1 = (8,"Solange",5.3)
tuple2 = 8,"Solange",5.3

print(type(tuple1))

c = (9,)
print(type(c))

d = (9)
print(type(d))

l = list(c)
print(l)

l.append(4)
print(l)

l = tuple(l)
print(l)

