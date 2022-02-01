"""
1) Este programa pide primeramente la cantidad total de compras de una persona.
Si la cantidad es inferior a $100.00, el programa dirá que el cliente no aplica
a la promoción. Pero si la persona ingresa una cantidad en compras igual o
superior a $100.00, el programa genera de forma aleatoria un número entero del
cero al cinco. Cada número corresponderá a un color diferente de cinco colores
de bolas que hay para determinar el descuento que el cliente recibirá como
premio. Si la bola aleatoria es color blanco, no hay descuento, pero si es uno
de los otros cuatro colores, sí se aplicará un descuento determinado según
la tabla que  aparecerá, y ese descuento se aplicará sobre el total de compra
que introdujo inicialmente el usuario, de manera que el programa mostrará un
nuevo valor a pagar luego de haber aplicado el descuento.

"""
import random
import time
def menu():
    print("sus gastos iguala o supera los 100 por lo tanto participa en la promocion. ")
    print("bola blanca = no tiene descuentos")
    print("bola roja 10%")
    print("bola azul 20%")
    print("bola verde 30%")
    print("bola amarilla 50%")
    print("el sistema esta obteniendo un resultado al azar...")
    time.sleep(2)
    print("........",end="")
    time.sleep(2)
    print("....",end="")
    time.sleep(2)
    print("........")
    time.sleep(2)
    print("")
    
    bola=random.randint(0,4)
    return bola
    
    


fin="s"
while fin=="s" or fin=="S":
    compra=int(input("ingrese monto de la compra:"))
    if compra<100:
        print("el cliente no aplica a la promocion.")
    else:
        bola=menu()
        if bola==0:
            print("obtuvo una bola blanca. no tiene descuentos,debe pagar",compra)
        elif bola==1:
            descuento=compra-(compra*10/100)
            print("obtuvo una bola roja. felicidades tiene un 10% de descuento,debe pagar",descuento)
        elif bola==2:
            descuento=compra-(compra*20/100)
            print("obtuvo una bola azul. felicidades tiene un 20% de descuento,debe pagar",descuento)
        elif bola==3:
            descuento=compra-(compra*30/100)
            print("obtuvo una bola verde. felicidades tiene un 30% de descuento,debe pagar",descuento)
        elif bola==4:
            descuento=compra-(compra*50/100)
            print("obtuvo una bola amarillo. felicidades tiene un 50% de descuento,debe pagar",descuento)









    fin=input("precione s para seguir")
    
print("fin.")    
