"""2) De la galería de productos, el usuario introducirá el código
y el número de unidades del producto que desea comprar.
El programa determinará el total a pagar, como una factura.
Una variante a este ejercicio que lo haría un poco más complejo
sería dar la posibilidad de seguir ingresando diferentes códigos
de productos con sus respectivas cantidades, y cuando el usuario
desee terminar el cálculo de la factura completa con todas sus compras"""
def galeria():
    print("1-camisa")
    print("2-cinturon")
    print("3-zapatos")
    print("4-pantalon")
    print("5-calcetines")
    print("6-faldas")
    print("7-gorras")
    print("8-sueter")
    print("9-corbata")
    print("10-chaqueta")
    codigo=input("introdusca codigo")
    return codigo
def eleccion(codigo):    
    precio={1:450,2:350,3:20,4:500,5:456,6:800,7:90,8:100,9:540,10:120}
    valor=precio[int(codigo)]
    return valor
def articulos(codigo):
    articulos={1:"camisa",2:"cinturon",3:"zapatos",4:"pantalones",5:"calcetines",6:"faldas",7:"gorras",8:"sueter",9:"corbata",10:"chaqueta"}
    nombre_articulo= articulos[codigo]
    return nombre_articulo
    
    


total=0
fin=""
while fin=="" :
    codigo=galeria()
    valor=eleccion(codigo)
    nombre_articulo=articulos(int(codigo))
    print("ud ingreso:",nombre_articulo," cuesta:", valor)
    
    cantidad =int(input ("ingrese cantidad"))
    subtotal=cantidad*valor
    print ("articulo:",nombre_articulo," precio unitario:", valor," cantidad:",cantidad," Total:", subtotal )
    
    total +=subtotal
    
    print ("total acumulado:",total)
    
    












    print("desea continuar comprando?")
    fin=input("desea continuar ENTER para continuar:")
