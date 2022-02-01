#para saber si es una palabra palindrome o sea que se escribe de un lado igual al otrdef inversion(palabra):

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

if palabra == inversion(palabra):
    print ("es palindrome")
else:
        print ("no es palindrome")
    
