def text_to_index(txt):
    txtDict = {}
    txtList = txt.split(" ")
    for i in range(0,len(txtList)):
        if(txtList[i] in txtDict):
            (txtDict[txtList[i]]).append(i)
        else:
            txtDict[txtList[i]]  = [i]
    return txtDict

str = "ceci est un texte un exemple de texte"
res = text_to_index(str)

print(res)

