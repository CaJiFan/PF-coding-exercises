#Realice un programa que imprima en pantalla el nombre del estudiante y si su promedio es mayor a 60 mostrar,
# "Aprobado", caso contrario mostrar "Reprobado"

#seguir formato, nombre, apellido, Estado:, aprobado/reprobado

#archivo grades.csv


# OUTPUT
#Aloysius Alfalfa    Estado: Aprobado
#University Alfred   Estado: Aprobado
#Gramma Gerty    Estado: Reprobado
#Electric Android    Estado: Reprobado
#....



#Solucion

file = open ("grades.csv","r")
file.readline()
linea = file.readline()
while linea!= "":
  datos = linea.split(",")
  suma = float(datos[3]) + float(datos[4]) + float(datos[5]) + float(datos[6]) +float(datos[7])
  if suma/5 <60:
    print(datos[1].strip(" "), datos[0], "\tEstado: Reprobado")
  else:
    print(datos[1].strip(" "),datos[0], "\tEstado: Aprobado")
  linea = file.readline()
file.close()