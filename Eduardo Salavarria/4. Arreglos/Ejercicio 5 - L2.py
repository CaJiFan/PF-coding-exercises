#Terminado

import numpy as np
estudiantes = ['Eduardo', 'Luisa', 'Juan', 'Roberta', 'Julia', 'Carmen', 'Andrea','Camila','Sebastian','Henry','Patricio','Danae', 'Dayana', 'Dana', 'Minerva','Joseline','Christian', 'Matias','Diego','Andres']

print(len(estudiantes))

notas_1 = [98, 91, 61, 56, 79, 64, 87, 82, 56, 77, 63, 95, 76, 66, 70, 12, 55, 75, 70, 94]
notas_2 = [70, 83, 60, 66, 68, 52, 65, 67, 20, 98, 96, 87, 50, 20, 63, 63, 66, 74, 66, 99]
notas_3 = [95, 87, 30, 83, 61, 58, 84, 66, 88, 91, 68, 78, 92, 90, 76, 55, 99, 20, 76, 88]

notas_1 = np.array(notas_1)
notas_2 = np.array(notas_2)
notas_3 = np.array(notas_3)

array_estudiantes = np.array(estudiantes)
#En la base de datos de los estudiantes se tienen las notas de 3 materias de la universidad y el nombre de los estudiantes en listas paralelas
#Con el uso de numpy defina las siguientes funciones:
#defina una funcion que nos ayude a determinar el promedio de las notas de los estudiantes para esto la funcion recibe como argumento a las 3 listas de notas

def promedioNotas(array_1,array_2,array_3):
    promedio = (array_1 +array_2 + array_3)/3
    return promedio

#Defina una funcion que con el uso de la funcion anterior nos ayude a saber el estado del estudiante. Si su promedio es mayor a 6 el estudiante tendra el
#estado de aprobado, si el estudiante tiene de promedio menor a 6 se sabra que estara reprobado.
#Los argumentos que recibe la funcion son las notas_1, notas_2, notas_3 y los estudiantes
#Output:
#>>>Estudiante Roberta, promedio: 9.75, status: Aprobado.

def status(array_1,array_2,array_3, estudiantes):
    promedio = promedioNotas(array_1, array_2, array_3)
    for index,promedio in enumerate(promedio):
        estudiante = estudiantes[index]
        if promedio<60:
            print(f"Estudiante: {estudiante}, promedio: {promedio:.2f}, status: Reprobado")
        else:
            print(f"Estudiante: {estudiante}, promedio: {promedio:.2f}, status: Aprobado")
        
#Defina una funcion cuadroHonor que tenga como argumento notas_1,notas_2, notas_3 y los nombres de los estudiantes
#E imprima por pantalla los 3 mejores estudiantes y muestre por pantalla su posicion de podium.
#Oro: Primer Lugar
#Plata: Segundo Lugar
#Bronce: Tercer Lugar
#
#Output:
#>>>Oro es para el estudiante Luis con un promedio 9.91
#>>>Plata es para el estudiante Maria con un promedio de 9.89
#>>>Bronce es para el estudiante Andrea con un promedio de 9.87

def cuadroHonor(array_1,array_2,array_3, estudiantes):
    #los 3 primeros
    promedio = promedioNotas(array_1, array_2, array_3)
    index_order = promedio.argsort()[::-1]
    print(index_order)
    promedios = promedio[index_order]
    print(promedios)
    estudiantes = estudiantes[index_order]
    print(estudiantes)
    # print(promedios)
    rangos = ['ORO','PLATA','BRONCE']
    for i in range(len(rangos)):
        print(f"{i+1}. {rangos[i]} es para el estudiante {estudiantes[i]} con un promedio de {promedios[i]}")

#Utilice cada una de las funciones
print(promedioNotas(notas_1,notas_2, notas_3))
status(notas_1,notas_2, notas_3, array_estudiantes)
cuadroHonor(notas_1,notas_2, notas_3, array_estudiantes)
