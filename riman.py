"""Ejercicio 3
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
últimas tiene que decir que riman un poco y si no, que no riman."""

palabra1=input("ingrese una palabra: ")
palabra2=input("ingrese otra palabra: ")
if len(palabra1)< 3 or len(palabra2)< 3:
        print("las palabras deben tener mas de 3 letras.")
    
if palabra1[-3:]==palabra2[-3:]:
    print ("riman")
elif palabra1[-2:]==palabra2[-2:]:
    print("riman un poco")
else:
    print("no riman.")
        
    

        
            
