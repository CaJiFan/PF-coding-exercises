import numpy as np
#Defina una funcion que con el uso de numpy nos ayude a saber cuales son los empleados que ganan mas de 300 dolares
def defVectores(l_empleados, l_sueldos, l_nombres):
  vEmpleados = np.array(l_empleados)
  vSueldos = np.array(l_sueldos)
  for i in range(vEmpleados.size):
    if vSueldos[i] > 300:
      l_nombres.append(vEmpleados[i])
  print("Empleados que ganan más de 300 dólares: ")
  for j in range(len(l_nombres)):
    print(l_nombres[j])

empleados = ['Eduardo', 'Minerva', 'Lissette'] 
sueldos = [900,500,250] 
nombres = []

defVectores(empleados, sueldos, nombres)