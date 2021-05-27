# Dada la siguiente lista guardar los elementos alfabeticamente en un archivo "archivo.txt", en el siguiente formato:


#kiwi
#manzana
#naranja
#pera
#sandia


#frutas = ["pera", "manzana", "kiwi", "sandia", "naranja"]

#Solucion

file = open ("archivo.txt","w")
frutas = ["pera", "manzana", "kiwi", "sandia", "naranja"]
frutas.sort()
for fruta in frutas:
  file.write(fruta+"\n")
file.close()