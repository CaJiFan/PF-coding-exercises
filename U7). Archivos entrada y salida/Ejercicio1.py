# sobre el archivo del quijote, escribir un programa que ponga todas las lineas del archivo en una lista de strings,
# quitar \n, mostrar por pantalla cuantas lineas y palabras contiene el archivo.


# archivo: el_quijote.txt

# OUTPUT:
#Total de lineas:  2186
#Total de palabras:  187019



#Solucion

file = open("el_quijote.txt","r")
linea = file.readline()
lista = []
while linea != "":
    lista.append(linea.strip("\n"))
    linea = file.readline()
file.close()
palabras = 0
for el in lista:
    pala = el.split(" ")
    palabras += len(pala)

print("Total de lineas: ", len(lista))
print("Total de palabras: ", palabras)