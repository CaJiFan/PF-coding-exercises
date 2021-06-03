#Terminado

#En su programa de python se pide que cree un vector que tenga un rango del -10 hasta el 10, pida al usuario un numero para determinar el tamaño del vector.
#Tambien el programa debe reemplazar los numeros menores a 0 por 1.

#Solucion
import numpy as np
size = int(input("Ingrese el tamano del vector"))
arreglo = np.random.randint(-10, 11,(size,), int)
print(arreglo)
for i in range(arreglo.size):
    if arreglo[i] <0:
        arreglo[i] = 1
print(arreglo)
