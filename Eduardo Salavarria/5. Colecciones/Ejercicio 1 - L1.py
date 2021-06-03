#Terminado

#En su uso de python se ha visto que las tuplas no pueden ser modificadas, sin embargo siempre hay una manera de poder modificarlas
#Use su razonamiento para poder modificiar el elemento o varios elementos de una tupla.

tupla = (1,2,3,4,5)
lista_tupla = list(tupla)
lista_tupla[0] = 5
tupla = tuple(lista_tupla)
print(tupla)

