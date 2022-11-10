gender = raw_input("Donner votre sexe (M/F) : ")

while gender != 'M' and gender != 'F' :
    print(gender == "M")
    gender = raw_input("Donner votre sexe (M/F) : ")

height = input("Donner votre taille (cm) : ")

while height < 0:
    height = input("Donner votre taille (cm) : ")

weight = input("Donner votre poids (kg) : ")

while weight < 0:
    weight = input("Donner votre poids (kg) : ")


masseCorporelle =  weight / ( height * height )

if (gender == "M" and  masseCorporelle > 25) or  (gender == "F" and  masseCorporelle > 23):
     print("Vous devriez surveiller votre alimentation")
elif (gender == "M" and  masseCorporelle < 19) or  (gender == "F" and  masseCorporelle > 18) :
     print("Vous devriez prendre des forces")
else:
    print("Vous etes a votre poids de forme")


