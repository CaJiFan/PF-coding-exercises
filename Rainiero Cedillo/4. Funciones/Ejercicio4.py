#Realiza una función separar(lista) que tome una lista de números enteros y devuelva dos listas ordenadas.
# La primera con los números pares y la segunda con los números impares. Probar la funcion y mostrar en pantalla
# las listas ordenadas
#NOTA: no alterar la lista ingresada

#lista = [2, 7, 8, 4, 78, 165, 74, -418, 0, 87, 65, 67, 17, 157]

# Output:
#Pares:  [2, 8, 4, 78, 74, -418, 0]
#Impares:  [7, 165, 87, 65, 67, 17, 157]


#solucion
def separar(lista):
  pares = []
  impares = []
  for elemento in lista:
    if (elemento%2 == 0 ):
      pares.append(elemento)
    else:
      impares.append(elemento)
  pares.sort()
  impares.sort()
  return pares, impares


lista = [2, 7, 8, 4, 78, 165, 74, -418, 0, 87, 65, 67, 17, 157]
v1,v2 = separar(lista)
print("Pares: ", v1)
print("Impares: ", v2)