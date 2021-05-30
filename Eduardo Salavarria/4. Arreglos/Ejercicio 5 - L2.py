import numpy as np
estudiantes = ['Eduardo', 'Luisa', 'Juan', 'Roberta', 'Julia', 'Carmen', 'Andrea','Camila','Sebastian','Henry','Patricio','Danae', 'Dayana', 'Dana', 'Minerva','Joseline','Christian', 'Matias','Diego','Andres']

print(len(estudiantes))

notas_1 = [98, 91, 61, 56, 79, 64, 87, 82, 56, 77, 63, 95, 76, 66, 70, 12, 55, 75, 70, 94]
notas_2 = [70, 83, 60, 66, 68, 52, 65, 67, 20, 98, 96, 87, 50, 20, 63, 63, 66, 74, 66, 99]
notas_3 = [95, 87, 30, 83, 61, 58, 84, 66, 88, 91, 68, 78, 92, 90, 76, 55, 99, 20, 76, 88]

array_nt1 = np.array(notas_1)
array_nt2 = np.array(notas_2)
array_nt3 = np.array(notas_3)

array_estudiantes = np.array(estudiantes)

#defina una funciones que saque un promedio de las notas
def promedioNotas(array_1,array_2,array_3):
    promedio = (array_1 +array_2 + array_3)/3
    return promedio


def status(array_1,array_2,array_3, estudiantes):
    promedio = promedioNotas(array_1, array_2, array_3)
    for index,promedio in enumerate(promedio):
        estudiante = estudiantes[index]
        if promedio<60:
            print(f"Estudiante: {estudiante}, promedio: {promedio:.2f}, status: Reprobado")
        else:
            print(f"Estudiante: {estudiante}, promedio: {promedio:.2f}, status: Aprobado")
        

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

print(promedioNotas(array_nt1,array_nt2, array_nt3))
status(array_nt1,array_nt2,array_nt3, array_estudiantes)
cuadroHonor(array_nt1,array_nt2,array_nt3, array_estudiantes)
