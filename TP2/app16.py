number = int(input("Donner un nombre : "))

for i in range(0,number):
    for j in range(0,4):
        print("*",end="")
    print("")

print("------------------------")

for i in range(0,number+1):
    for j in range(0,i):
        print("*",end="")
    print("")

print("------------------------")

for i in range(0,number):
    for j in range(0,number):
        if (i == 0 or i == number-1):
            print("*",end="")
        else:
            if(j == 0 or j == number-1):
                 print("*",end="")
            else:
                print(" ",end="") 
    print("")

print("------------------------")  

for i in range(0,number):
    for j in range(0,i+1):
        if(i>1 and i  < number-1 ):
            if(j==0 or j==i):
                print("*",end="")
            else:
                print(" ",end="")
        else:
            print("*",end="")
    print("")  

