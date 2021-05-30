#Borrador
#usando for
materias = []
notas = []

for index in range(3):
    materia = input("Ingrese el nombre de la materia ")
    nota = float(input("Ingrese la nota de la materia: "))
    materias.append(materia)
    notas.append(nota)

promedio = sum(notas)/len(notas)

index_mejorProm = notas.index(max(notas))
print(f"La materia con mejor promedio es {materias[index_mejorProm]} con una calificacion de {notas[index_mejorProm]}")
print('Su promedio es:', promedio)
if (promedio>6):
    print("Usted acaba de pasar el semestre con exito")
else:
    print("Usted acaba de reprobar el semestre")

