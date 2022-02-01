def Abinario(decimal):
    resultados=[int(decimal)]
    residuos=[2]
    i=0
    #jkalskdj
    if int(decimal) != 0:
        while resultados[i] != 0:
            residuos[i] = resultados[i]%2
            resultados.append(resultados[i]//2)
            residuos.append(2)
            i=i+1
        residuos.pop()
    else:
        residuos[0]=0
    binario=list(reversed(residuos))        
    return binario

def Adecimal(binario):
    invertido=list(reversed(binario))
    posicion=0
    decimal=0
    for i in invertido:
        decimal= decimal + (int(i)*(2**posicion))
        posicion=posicion +1
    return decimal

menu=1
while menu!=0:
    print ("\n ***conversor***")
    opcion = input("1- decimal a binario.\n2- binario a decimal.\n0- terminar.\nIngrese opcion: ")
    if opcion == "1":
        decimal = input("Ingrese un numero decimal: \n")
        print(*Abinario(decimal),sep='')
        
    elif opcion =="2":
        binario= input("ingrese numero binario: \n")
        print (Adecimal(binario),sep='')
    elif opcion == "0":
        print("Fin.")        
        break
    else:
        print ("opcion no admitida")

                   
