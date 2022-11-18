daysNumber = [31,28,31,30,31,30,31,30,28,30,31,30]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',  'August', 'September', 'October', 'November', 'December']
res = []
for d,m in zip(months,daysNumber):
    res.append(str(d)+" "+m)
print(res)
  