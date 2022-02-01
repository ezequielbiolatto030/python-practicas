def MasLarga (lista):
    if lista==[]:
        palabra ="no se encontro ninguna palabra ingresada"
        return (palabra)
    else:
        palabra=""
        print("la palabra mas larga es: " )
        for i in lista:           
            if len(i) > len(palabra):
                palabra= i
        return (palabra)
    
            
lista=[]
elemento="1"
while elemento!="":
    elemento =  input ("ingrese palabra o precione enter para terminar: ")
    lista.append(elemento)
lista.pop()
print(MasLarga(lista))
