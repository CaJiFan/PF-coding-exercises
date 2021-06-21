#Dadas las siguientes listas defina la funcion matriz() que recibe las 3 listas y devuelve como resultado
# una matriz donde se encuentran los datos que corresponden a su columna y fila. Sin embargo, el resto de
# espacios deberan ser 0. Retorne la matriz y el promedio de toda la matriz.

#filas = [1,2,7,5,4,6,9,8,3,0]
#columnas = [1,2,2,2,4,8,7,5,3,7]
#datos = [78,74,24,68,12,87,98,45,87,56]


# OUTPUT
#[[ 0.  0.  0.  0.  0.  0.  0. 56.  0.  0.]
# [ 0. 78.  0.  0.  0.  0.  0.  0.  0.  0.]
# [ 0.  0. 74.  0.  0.  0.  0.  0.  0.  0.]
# [ 0.  0.  0. 87.  0.  0.  0.  0.  0.  0.]
# [ 0.  0.  0.  0. 12.  0.  0.  0.  0.  0.]
# [ 0.  0. 68.  0.  0.  0.  0.  0.  0.  0.]
# [ 0.  0.  0.  0.  0.  0.  0.  0. 87.  0.]
# [ 0.  0. 24.  0.  0.  0.  0.  0.  0.  0.]
# [ 0.  0.  0.  0.  0. 45.  0.  0.  0.  0.]
# [ 0.  0.  0.  0.  0.  0.  0. 98.  0.  0.]]
#Promedio:  6.29

#solucion
import numpy as np

def matriz(filas, columnas, datos):
  matriz = np.zeros((len(filas),len(columnas)))
  for ind in range(len(datos)):
    matriz[filas[ind],columnas[ind]] = datos[ind]
  return matriz, matriz.mean()


filas = [1,2,7,5,4,6,9,8,3,0]
columnas = [1,2,2,2,4,8,7,5,3,7]
datos = [78,74,24,68,12,87,98,45,87,56]

M,prom = matriz(filas, columnas, datos)
print(M)
print("Promedio: ", prom)