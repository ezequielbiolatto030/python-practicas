
lista=[]
numero=1
while numero != "":
    numero = input ("Vamos a ingresar los numeros.. \n ingrese un numero o precione enter para terminar: ")
    lista.append(numero)
    
lista.pop()
print ("el mayor de:")
print (lista)
print (max(lista))

