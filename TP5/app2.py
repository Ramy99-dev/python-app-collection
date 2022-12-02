
def difference(l):
    m = []
    for i  in range(0,len(l)-1) :
       m.append(l[i+1]-l[i])
    
    return m

def itere(l,n):
    if(n == 0):
        return l
    elif(n == 1):
        return difference(l)
    else:
        return difference(difference(l))

l = [2,7,10,23,27]
print(l)

res = difference(l)
print(res)

res = itere(l,2)
print(res)