#Reemplazar los numeros menores a 0 por 1
#Cree un vector random y cambie los valores que sea menor a 0 por 1

import numpy as np
size = int(input("Ingrese el tamano del vector"))
arreglo = np.random.randint(-10, 11,(size,), int)
print(arreglo)
for i in range(arreglo.size):
    if arreglo[i] <0:
        arreglo[i] = 1
print(arreglo)
