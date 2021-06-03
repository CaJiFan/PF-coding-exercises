#Terminado

#Ejercicio 1
#Realice un programa para determinar si un numero es par o no
#muestre en pantalla "es numero par" o "es numero impar"

#Solucion
numero = int(input("Ingrese un numero"))
if (numero%2 == 0):
    print("El numero es par")
else:
    print("El numero es impar")


#Ejercicio 2
#Cree un programa que en la que el usuario pueda ingresar una oracion e imprima cada palabra de la oracion

#Solucion
oracion = input("Ingrese una oracion")
list_oracion = oracion.split(" ")
for palabra in list_oracion:
    print(palabra)