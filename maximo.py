def max (numUno, numDos):
    if numUno < numDos:
        maximo = numDos
    elif numUno > numDos:
        maximo = numUno
    elif numUno == numDos:    
        maximo = "los numeros son iguales"
    return maximo
numUno = input("Ingrese un primer numero: ")
numDos = input("ingrese el segundo:")
mayor= max (numUno,numDos)
print(mayor)


