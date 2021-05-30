import numpy as np
#Cree un programa que pida al usuario ingresar el numero de filas y columnas de un arreglo numpy y sustituya todas las esquinas del arreglo por 1


filas = int(input("Ingrese un número para las filas: "))
columnas = int(input("Ingrese un número para las columnas: "))
arregloFC = np.zeros((filas, columnas), int)
arregloFC[0, 0] = 1
arregloFC[0, -1] = 1
arregloFC[- 1, - 1] = 1
arregloFC[- 1, 0] = 1
print(arregloFC)