#ejercicio 3 maximo de tres
def max_de_tres (n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print (n1)
    elif n2 > n1 and n2 > n3:
        print (n2)
    elif n3 > n1 and n3 > n2:
        print (n3)
    else:
        print ("Son iguales")
    


n1= input ("ingrese numero A: ")
n2= input ("ingrese numero B: ")
n3= input ("ingrese numero C: ")

max_de_tres(n1,n2,n3)

