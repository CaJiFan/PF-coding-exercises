#Terminado

#En una empresa le piden a usted crear un programa que nos ayude a determinar los nombres de los empleados que ganan mas de 300 dolares
#dentro de la empresa, para ello nos dan una lista de nombre de los empleados y los sueldos de cada uno de ellos
#Defina una funcion que con el uso de numpy nos ayude a saber cuales son los empleados que ganan mas de 300 dolares, determine tambien los argumentos que va a usar

import numpy as np
empleados = ['Dana', 'Diego', 'Daniel'] 
sueldos = [900,500,250] 
nombres = []

#Solucion
def defVectores(l_empleados, l_sueldos, l_nombres):
  vEmpleados = np.array(l_empleados)
  vSueldos = np.array(l_sueldos)
  for i in range(vEmpleados.size):
    if vSueldos[i] > 300:
      l_nombres.append(vEmpleados[i])
  print("Empleados que ganan más de 300 dólares: ")
  for j in range(len(l_nombres)):
    print(l_nombres[j])

defVectores(empleados, sueldos, nombres)