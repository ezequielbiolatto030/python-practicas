#longitud de una palabra
def largo_cadena (lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont
lista = str(input ("ingrese una palabra: "))
print("la palabra " + lista + " tiene " ,largo_cadena(lista), " caracteres")
