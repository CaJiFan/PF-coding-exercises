#de una manera ingeniosa cambie los valores de una tupla

tupla = (1,2,3,4,5)
lista_tupla = list(tupla)
lista_tupla[0] = 5
tupla = tuple(lista_tupla)
print(tupla)

