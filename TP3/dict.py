myDict = {"pomme":21 , "melon":3 ,"poire":31}

for value in myDict.values():
    print(value)
for key in myDict.keys():
    print(key)

if 21 in myDict.values():
    print("Un des fruits se trouve dans la qté ")

for key,value in myDict.items():
    print("Dans le clé " , key , "il y'a la value " , value )
