#Terminado

#Usted cree un programa en el que pueda usarlo como calculadora de operaciones basicas (suma, resta, multiplicacion, division)
#La operacion debe ingresarse de una manera muy peculiar, el igreso del usuario es el siguiente (con el uso de +,-,*,/) respectivamente
#para cada una de las operaciones

#Ingrese una operacion:
#2+2
#>>>El resultado de la suma es: 4

#OBSERVE que la unica linea ingresada por el usuario es la que determina la operacion.
#Defina funciones de suma, resta, multiplicacion y division.
#Defina funciones para poder saber cuales son los numeros ingresados (recuerde que tambien pueden ser float)

#Solucion
from funciones import *
usuario = input("ingrese una operacion")
num_1, num_2, operacion = operacion(usuario)
if operacion == "+":
    respuesta = suma(num_1,num_2)
    print(num_1, operacion, num_2,"=", respuesta)
elif operacion =="-":
    respuesta = resta(num_1,num_2)
    print(num_1, operacion, num_2,"=", respuesta)
elif operacion == "*":
    respuesta = multiplicacion(num_1,num_2)
    print(num_1, operacion, num_2,"=", respuesta)
elif operacion == "/":
    respuesta = division(num_1,num_2)
    print(num_1, operacion, num_2,"=", respuesta)
