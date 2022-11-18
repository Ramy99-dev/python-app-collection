list1 = ["Lundi" , "Mardi"]
list2 = [ "Mercredi","Jeudi"]
list3 = ["Vendredi","Samedi","Dimanche"]

week1 = list1 + list2[1:] + list3
week2 = list1 + list2 + list3[:2]

print(week1)
print(week2)
