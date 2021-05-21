#Usted recibe las variables texto1 y texto2 que tiene una separacion con un caracter especial "|". 
#En el texto1 se encuentran las calificaciones y en el texto2 que contiene los estudiantes de igual manera.
#Determine una manera en que pueda sacar dos listas distintas y hacer lo siguiente:

#determine cuantos estudiantes hay en el paralelo
#Determine cual fue el estudiante con mejor calificacion y muestre en pantalla su calificacion
#Con la libreria random muestre en pantalla un estudiante al azar con su calificacion

import random as rd

texto1 = "9.9|9.8|7.5|6.4|9|5.4|5|6.7|9.2|8.3"
texto2 = "Eduardo|Maria|Diego|Juan|Angel|Daniel|Sebastian|Andrea|Mateo|Emily"

notas = texto1.split("|")
estudiantes = texto2.split("|")

ind_max = notas.index(max(notas))
mejor_est = estudiantes[ind_max]

print(f"El mejor estudiante es {mejor_est} con una calificacion de {max(notas)}")
num_azar = rd.randrange(len(notas))
print(f"El estudiante escogido al azar fue {estudiantes[num_azar]} con una calificacion de {notas[num_azar]}")
