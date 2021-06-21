#Dada la siguiente lista de numeros muestre en pantalla unicamente los numeros pares utilizando for o while

# lista = [20, 18, 45, 174, 16, 33, 14, 15, 78, 64, 66, 31, 11, -71, -98, -2]

#Ejemplo:

# OUTPUT
#20
#18
#174
#16
#14
#78
#64
#66
#-98
#-2

#solucion

lista = [20, 18, 45, 174, 16, 33, 14, 15, 78, 64, 66, 31, 11, -71, -98, -2]
for numero in lista:
  if numero%2 == 0:
    print(numero)