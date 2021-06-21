#Realice un programa donde se registra el nombre del articulo y la cantidad que se vendio (se pueden repetir articulos
# y cantidades). Tiene que guardarlas en una lista en un formato indicado. Solo si el usuario ingresa un 0 como nombre
# del articulo finaliza el programa y muestra la lista de ventas.

#NOTA: sin importar como escriba el nombre el usuario usted debe guardarlo en mayusculas. Y suponga que el usuario solo
# ingresara numeros como cantidad (no validar si ingresa letras)

#Ejemplo:

#Bienvenido al programa de ventas
#Ingrese el nombre del articulo vendido: mesa
#Ingrese la cantidad vendida del articulo anterior: 2
#Venta agregada:  MESA-2

#Ingrese el nombre del articulo vendido: vasos
#Ingrese la cantidad vendida del articulo anterior: 4
#Venta agregada:  VASOS-4

#Ingrese el nombre del articulo vendido: 0

#['MESA-2', 'VASOS-4']
#GRACIAS



#solucion

ventas = []

nombre = ""
print("Bienvenido al programa de ventas")
while nombre!= "0":
  nombre = input("Ingrese el nombre del articulo vendido: ")
  nombre = nombre.upper()
  if nombre!="0":
    cantidad = input("Ingrese la cantidad vendida del articulo anterior: ")
    venta = nombre+"-"+cantidad
    ventas.append(venta)
    print("Venta agregada: ", venta)
  print()
print(ventas)
print("GRACIAS")