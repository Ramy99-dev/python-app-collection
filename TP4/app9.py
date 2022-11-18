phrase = input("Donner une phrase : ")

pourcentage = {}

for i in phrase :
    if i in pourcentage:
        pourcentage[i] += 1
    else :
        pourcentage[i] = 1

for word,number in pourcentage.items():
    print("Le pourcentage d'appartition du caractére {0} est {1} %".format(word,(number/len(phrase)*100)))