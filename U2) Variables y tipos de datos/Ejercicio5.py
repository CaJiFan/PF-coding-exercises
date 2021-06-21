#Dadas las listas de estudiantes y de edad de un curso muestre por pantalla lo siguiente:
#Promedio de la edad de los estudiantes, el estudiante con la mayor edad y otro estudiante con la menor edad.

# estudiantes = ["Juan", "Pedro", "Maria","Eduardo", "Jose", "Paola"]
# edades = [19, 18, 18, 18, 17, 20]

#Ejemplo:

# OUTPUT
# Jose es el estudiante con menor edad
# Paola es el estudiante con mayor edad
# Promedio de edad de los estudiantes del curso: 18.33

#solucion

estudiantes = ["Juan", "Pedro", "Maria","Eduardo", "Jose", "Paola"]
edades = [19, 18, 18, 18, 17, 20]

indMax = edades.index(max(edades))
indMin = edades.index(min(edades))

print(estudiantes[indMin], "es el estudiante con menor edad")
print(estudiantes[indMax], "es el estudiante con mayor edad")
print("Promedio de edad de los estudiantes del curso: ", sum(edades)/len(edades))