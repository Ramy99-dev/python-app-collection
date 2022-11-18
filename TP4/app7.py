ch = "un bon étudient est celui qui révise chaque jour son cours"

pos1 = ch.find("bon")
ch1 = ch[pos1:pos1 + len("bon")]
print(ch1)

ch2 = ch[0 :pos1 + len("bon")] +" "+ ch1*2

print(ch2)