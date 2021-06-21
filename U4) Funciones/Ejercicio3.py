#Defina la funcion rectangulo(altura, anchura) que imprima en pantalla un rectangulo formado por el signo *.
# Pedir los datos por consola (no va dentro de la función) y probar la funcion
#NOTA: suponer que el usuario solo ingresara numeros naturales

# Ejemplo:
# Ingrese la altura del rectangulo: 4
# Ingrese la anchura del rectangulo: 6
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *


#solucion
def rectangulo(altura, anchura):
  for a in range(altura):
      for b in range(anchura):
          print("* ", end="")
      print()


altura= int(input("Ingrese la altura del rectangulo: "))
anchura= int(input("Ingrese la anchura del rectangulo: "))
rectangulo(altura, anchura)