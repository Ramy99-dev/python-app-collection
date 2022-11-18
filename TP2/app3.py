hourNumber = int(input("Donner le nombre des heures : "))
hourAmount = float(input("Donner le montant d'une heure "))

amount = 0

if hourNumber == 39 :
    amount = 0
elif hourNumber < 45:
    amount = (hourNumber - 39) * (hourAmount * 1.5) 
elif hourNumber < 49:
    amount = 5*hourAmount*1.5 + (hourNumber - 45) * (hourAmount * 1.75) 
else : 
    amount = 5*hourAmount*1.75 + 5*hourAmount*1.5  + (hourNumber - 49) * (hourAmount * 2)

print(amount)