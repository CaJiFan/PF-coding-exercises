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
