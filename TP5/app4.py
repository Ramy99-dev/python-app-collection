def polyvaleur(listpoly , x):
    res = 0 
    for i in listpoly:
        res += (i*(x**(listpoly.index(i))))
    return res

def polyaddition(listpoly1 , listpoly2):
    listPolySomme = []

    length = 0
    if(len(listpoly1) > len(listpoly2)):
        length = len(listpoly1)
    else:
        length = len(listpoly2)
    
    for i in range(0,length):
        if(i < len(listpoly1)-1 or i < len(listpoly2)-1):
            listPolySomme.append(listpoly1[i] + listpoly2[i])
        else:
            if(i>len(listpoly1)):
                 listPolySomme.append(listpoly2[i])
            else:
                 listPolySomme.append(listpoly1[i])
    return listPolySomme

def polyaffiche(listpoly):
    poly = ""
    for i in listpoly:
        if(listpoly.index(i) != 0):
            if(i != 0):
                poly+= str(i)+"x^"+str(listpoly.index(i)) +"+"
            elif(listpoly.index(i) == len(listpoly)-1):
                 poly+= str(i)+"x^"+str(listpoly.index(i)) 
        else:
          poly += str(i)+"x"+"+"
    return poly


print(polyvaleur([1,0,2,3],2))
print(polyaddition([1,2,5],[3,4]))
print(polyaffiche([3,0,4,0,2]))
