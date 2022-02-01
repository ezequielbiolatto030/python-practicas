print("programa para sacar precios de venta")

x=1
while x==1:
    producto= input ("ingrese descripcion del producto: ")
    cantidad= int(input ("ingrese cantidad comprada: "))
    costo= int (input ("ingrese el costo: "))
    venta = int(((((costo / cantidad) * 1.17)*1.21)*1.35))
    print("")
    print ("<<<<", producto,":",venta,">>>>")
    opcion= input("precione 2 para terminar")
    if opcion == "2":
                x=x+1
print("fin")
                
            

    
                
