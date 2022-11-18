phrase = input("Donner une phrase : ")

voyelle = ('aeiouy') 
sommeVoyelle = 0

for i in phrase :
    if(i.lower() in voyelle):
        sommeVoyelle += 1

print(sommeVoyelle)
