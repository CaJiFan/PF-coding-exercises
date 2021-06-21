#Realice un programa donde se realiza un sorteo entre las vocales y le pide al usuario que ingrese una vocal y mostrar
# por pantalla si gano el sorteo y cual fue el la vocal ganadora
#NOTA: el usuario va ingresa letras en mayúsculas
#Ejemplo:

# INPUT
# Ingrese una vocal: E

# OUTPUT
# GANO: False
# Vocal ganadora: I

#solucion

import random

vocales = ["A","E","I","O","U"]
vocal = input("Ingrese una vocal: ")
indiceRandom = random.randint(0,len(vocales)-1)
ganador = vocales[indiceRandom]

print("GANO: ", vocal==ganador)
print("Vocal ganadora: ", ganador)