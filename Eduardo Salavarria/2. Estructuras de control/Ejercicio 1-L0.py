#Borrador
#Estructura de control if

#Realice un programa para determinar si un numero es par o no
#muestre en pantalla "es numero par" o "es numero impar"

numero = int(input("Ingrese un numero"))

if (numero%2 == 0):
    print("El numero es par")
else:
    print("El numero es impar")

#Pida al usuario una oracion, e imprimir cada palabra de la oracion
oracion = input("Ingrese una oracion")
list_oracion = oracion.split(" ")
for palabra in list_oracion:
    print(palabra)