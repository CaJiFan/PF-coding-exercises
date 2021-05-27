# Dado el archivo compras.txt leer el archivo y mostrar en pantalla la lista de tuplas con objetos y cantidades de
# la siguiente forma


#OUTPUT

#[('rosas', 15), ('manzanas', 5), ('peras', 10), ....]


#Solucion
file = open ("compras.txt","r")
lista = []
linea = file.readline()
while linea!= "":
  datos = linea.split("|")
  tupla = (datos[0], int(datos[1]))
  lista.append(tupla)
  linea = file.readline()
file.close()

print(lista)

