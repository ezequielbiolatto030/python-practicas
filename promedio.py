nombre= input("como te llamas: ")
print ("Hola ", nombre, "ahora ingresa las calificaciones: ")
cali_biol = int(input("calificacion de biologia: "))
cali_mate = int (input("calificacion de matematica: "))
cali_leng = int (input("calificacion de lengua: "))
promedio= float((cali_biol + cali_mate + cali_leng )/ 3)
if promedio >= 6 :
    print("excelente aprobaste!! tu promedio es: ", promedio)
print("fin")
