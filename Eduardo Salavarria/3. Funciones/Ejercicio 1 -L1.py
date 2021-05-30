
#defina una funcion para registrar a los estudiantes con sus notas 
#Defina una funcion que reciba una lista de las notas y de los nombres y determine el mejor estudiantes
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

