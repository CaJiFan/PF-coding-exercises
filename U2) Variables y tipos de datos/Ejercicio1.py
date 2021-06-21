#Realice un programa que pida al usuario que ingrese un número de horas, minutos y días, y muestre en pantalla el número
# total de minutos de todos los datos ingresados.
#NOTA: suponga que el usuario solo va a ingresar numeros enteros positivos
#Ejemplo:

# INPUT
# Ingrese Numero de minutos : 30
# Ingrese Numero de Horas : 40
# Ingrese Numero de dias: 1

# OUTPUT
# Numero total de minutos: 3870 

#solucion

minutos = int(input("Ingrese el numero de minutos: "))
horas = int(input("Ingrese el numero de horas: "))
dias = int(input("Ingrese el numero de dias: "))

horasmin = horas*60
diasmin = dias*60*24

print("Numero total de minutos:", minutos+horasmin+diasmin)