#Realice un progrma que simule un juego de azar, muestre por pantalla un bienvenida, pida al usuario ingresar un numero
# del 1 al 5, y si adivina el numero que la maquina toma aleatorio suma un punto y un mensaje de felicidades. Y si no
# acierta, muestra un mensaje de continuar. El juego solo termina si el usuario ingresa 0 como numero.

#NOTA: Existen 2 casos, donde gana (suma punto y muestra mensaje1) y donde pierde (no suma puntos y muestra mensaje2).
#Solo en caso de que no acierte, debe mostrar el numero que no acerto

#Ejemplo:

# OUTPUT
#Bienvenido al programa
#Ingrese un número: 1

#Sigue intentando
#El numero era:  2
#Puntos:  0
#Ingrese un número: 3

#Has acertado
#Puntos:  1
#Ingrese un número: 0

#Puntos:  0
#GAME OVER


#solucion

import random

numero = 1
puntos = 0
print("Bienvenido al programa")
while numero!= 0:
  numero = int(input("Ingrese un número: "))
  print()
  numeroRand = random.randint(1,5)
  if numero ==numeroRand:
    puntos+=1
    print("Has acertado")
  elif numero!=0:
    print("Sigue intentando")
    print("El numero era: ", numeroRand)
  print("Puntos: ", puntos)

print("GAME OVER")