#Reino del Dragon....
import random
import time


 
def introduccion():
 print ("Estamos en una tierra llena de dragones. Delante de nuestro,")
 print ("se ven dos cuevas. En una cueva, el dragon es amigable")
 print ("y compartira el tesoro contigo. El otro dragon")
 print ("es codicioso y hambriento, y te va a comer ni bien te vea.")
 print ("")

def CambiarCueva():
 cueva = ""
 while cueva != "1" and cueva != "2":
  print ("Ha que cueva quieres entrar? 1 o 2?")
  cueva = input()

 return cueva

newgame = ("s")
oro = 0

while newgame == ("s"):

 NumdelaCueva = CambiarCueva()

 print ("Te acercas a la Cueva...")
 #time.sleep(2)
 print ("Esta oscuro y tenebroso...")
 #time.sleep(2)
 print ("Un gran dragon salta delante tuyo, abre su boca y...")
 print ("")
 #time.sleep(2)

 FriendlyCueva = random.randint (1, 2)
 print ("la cueba es", FriendlyCueva)


 
 if NumdelaCueva == str(FriendlyCueva):
  print ("Te entrega el tesoro...")
  cofre = random.randint(50, 200)
  print ("Has ganado ", cofre, "en oro")
  oro += cofre
 else:
  print ("El dragon te come de un bocado....")
  print ("Perdiste!!nOro acomulado:", oro)
  newgame = input("Quieres jugar de nuevo? (s / n)")

  oro = 0



 



