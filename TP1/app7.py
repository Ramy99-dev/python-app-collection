h = int(input("Hours : "))

while h > 24 : 
    h = int(input("Hours : "))

m = int(input("minutes : "))


while m > 59 : 
    m = int(input("minutes : "))
    
s = int(input("seconds : "))


while s > 59 : 
    s = int(input("seconds : "))


print('{:02d}:{:02d}:{:02d}'.format(h,m,s))

s+=1

if(s == 60):
    s = 0
    m+=1
if(m == 60):
    m = 0
    h+=1
if(h == 24):
    h = 0

print('{:02d}:{:02d}:{:02d}'.format(h,m,s))    

