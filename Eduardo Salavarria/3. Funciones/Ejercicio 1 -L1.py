#Terminado

#En una institucion se necesita registrar a cada estudiantes y por eso el director le pide a usted crear un programa de python
#que le permita realizar esto.
#Defina una funcion  que le ayude a registrar a los estudiantes con sus notas, esta funcion recibe de argumentos la lista nombres, lista de notas
#el nombre y la nota del estudiante a registar
#Defina una funcion que reciba una lista de las notas y de los nombres y retorne el nombre del mejor estudiante.
#Muestre por pantalla el resultado de las funciones.

#Solucion
nombres = []
notas = []


def registroEstudiante(l_nombres, l_notas, nombre, nota):
    nombre.append(l_nombres)
    nota.append(l_notas)
    print("Se ha registrado el estudiante")

def mejorEstudiante(l_nombres, l_notas):
    index_max = l_notas.index(max(l_notas))
    mejor_estudiante = l_nombres[index_max]
    return mejor_estudiante

