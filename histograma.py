def procedimiento(numero):
    for i in numero:
        for x in range(int(i)):
            print ("*", end="")
        print("\n")

numero= input ("ingrese un numero entero: ")
procedimiento(numero)
        
