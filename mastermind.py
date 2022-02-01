
"""Escribe un programa que te permita jugar a una versión simplificada del
juego Master Mind. El juego consistirá en adivinar una cadena de números
distintos. Al principio, el programa debe pedir la longitud de la cadena (de 2
a 9 cifras). Después el programa debe ir pidiendo que intentes adivinar la
cadena de números. En cada intento, el programa informará de cuántos números
han sido acertados (el programa considerará que se ha acertado un número si
coincide el valor y la posición).

Dime la longitud de la cadena: 4
Intenta adivinar la cadena: 1234
Con 1234 has adivinado 1 valores. Intenta adivinar
la cadena: 1243
Con 1243 has adivinado 0 valores. Intenta adivinar
la cadena: 1432
Con 1432 has adivinado 2 valores. Intenta adivinar
la cadena: 2431
Con 2431 has adivinado 4 valores.
Felicidade >>>"""

#time.sleep(2)
import random
import time
def comprobar(numero_ingresado,numero_secreto):
    x=0
    aciertos=""
    for i in numero_ingresado:
        if numero_secreto.find(i,x,x+1)==-1:
            aciertos+="#"
        else:
            aciertos+=i

        x=x+1
    print (aciertos)
    return aciertos
def ingreso(numero_ingresado,longitud):
    if len(numero_ingresado)== int(longitud):
        print("el numero ingresado esta siendo procesado..")
        time.sleep(2)
        return "ok"
       
    else:
        print("intente de nuevo. el numero debe ser de ", longitud,"digitos.")
        
        return "no"

#aca creo el numero secreto aleatoriamente
longitud=input("Nivel:ingrese longitud de la cadeana de 2 a 9 digitos:")
numero_secreto=""
print("creando numero secreto de ",longitud," digitos..." )
time.sleep(2)
for i in range(int(longitud)):
    numero_secreto+= str( random.randint (0, 9))
print("listo. numero secreto guardado.")


numero_ingresado=input("ingrese numero")

cont=1
while numero_ingresado!=numero_secreto:
    if ingreso(numero_ingresado,longitud)=="ok":
        if comprobar(numero_ingresado, numero_secreto)== numero_secreto: #aciertos==numero_secreto
            break
        else:
            numero_ingresado=input("vuelva a intentarlo..ingrese numero")
            cont=cont+1
            comprobar(numero_ingresado,numero_secreto)
            
            
        
    else:
        numero_ingresado=input("ingrese numero")
print("felicidades  ud a acertado en", cont, "veces")
        
        
        
    
    


    
    
    
        
    

