"""Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas,
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones
por las tres ventas que realiza en el mes y el total que recibirá en el mes
tomando en cuenta su sueldo base y comisiones."""

sueldo =int(input("sueldo"))
venta1 = int(input("venta1"))
venta2 = int(input("venta2"))
venta3 = int(input("venta3"))

comiciones = venta1//10 +venta2//10 + venta3//10
print ("comiciones",comiciones)
total = sueldo+comiciones
print ("sueldo mas comisiones",total )


