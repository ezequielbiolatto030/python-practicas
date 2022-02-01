def superposicion(lista1, lista2):
    
    if len(lista1)<= len(lista2):
        menor=lista1
    else:
        menor=lista2
    indice=0
    resultado= False
    for i in menor:
        if lista1[indice:indice+1] == lista2[indice:indice+1]:
            resultado = True
            break
        else:
            indice=indice +1
        
    return (resultado)

lista1=input ("ingrese una palabra: ")
lista2=input ("ingrese una palabra a comparar: ")
print("hay un elemento que se superponga en la misma ubicacion?")
print(superposicion(lista1, lista2))
        


            
         
