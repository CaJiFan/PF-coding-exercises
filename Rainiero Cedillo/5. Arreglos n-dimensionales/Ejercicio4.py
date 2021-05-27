#Dadas 2 listas de calificaciones de 2 cursos de una materia, defina la funcion promedio() que calcule
# el promedio utilizando arreglos, retorne el arreglo de la union de las listas (ordenado de mayor a menor)
# y el promedio de las calificaiones de la materia

#lista1 = [1,1,9,5,4,2,5,1,0,9,9,5,7,9,5]
#lista2 = [9,2,3,0,9,3,2,7,6,9,7,1,2,6,6]


# output
#[0 0 1 1 1 1 2 2 2 2 3 3 4 5 5 5 5 6 6 6 7 7 7 9 9 9 9 9 9 9]
#Promedio:  4.8

#solucion
import numpy as np


def promedio(lista1, lista2):
  arr1 = np.array(lista1)
  arr2 = np.array(lista2)
  arreglo = np.concatenate((arr1,arr2))
  return np.sort(arreglo), arreglo.mean()


lista1 = [1,1,9,5,4,2,5,1,0,9,9,5,7,9,5]
lista2 = [9,2,3,0,9,3,2,7,6,9,7,1,2,6,6]

arr,prom = promedio(lista1, lista2)
print(arr)
print("Promedio: ", prom)