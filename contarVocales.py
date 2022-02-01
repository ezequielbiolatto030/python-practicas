#contador de vocales
palabra =input ("ingres una palabra")
palabra = palabra.lower()#paso toda la palabra a minuscula
vocala=0
vocale=0
vocali=0
vocalo=0
vocalu=0
for i in palabra:
    if i == "a" :
        vocala=vocala+1
    elif i == "e":
        vocale=vocale+1
    elif i== "i":
        vocali=vocali+1
    elif i== "o":
        vocalo=vocalo+1
    elif i== "u":
        vocalu=vocalu+1
print("tiene ",vocala," a, ",vocale," e, ",vocali," i, ",vocalo," o ",vocalu," u.")
    
