#inversion de una cadena

def inversion(palabra):
    longitud= len(palabra)
    palabrainvertida= ""
    for i in palabra:
        letra=palabra[longitud-1:longitud]
        palabrainvertida = palabrainvertida + letra
        longitud=longitud-1
    return palabrainvertida
palabra= input ("ingrese palabra")
print(inversion(palabra))

    
