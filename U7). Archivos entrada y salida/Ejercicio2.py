# Dado el archivo deniro.csv realice un programa que muestre por pantalla el promedio de score de todas las peliculas
# de Robert De Niro

#OUTPUT
#Promedio de Score:  58.195


#solucion
import numpy as np
file = open ("deniro.csv","r")
file.readline()
linea = file.readline()
score = []
while linea!= "":
  datos = linea.split(",")
  score.append(int(datos[1]))
  linea = file.readline()
file.close()
array = np.array(score)
print("Promedio de Score: ", round(array.mean(),3))