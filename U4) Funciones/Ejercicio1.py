#Dadas las 2 siguientes listas (dias de trabajo y la cantidad de trabajadores que asistieron ese dia), defina la funcion
# ordenar(l1, l2) que recibe las 2 listas y devuelve como resultado una lista con los días ordenados de mayor a menor
# segun el numero de trabajadores que asistieron. Al final pruebe la función y verifique que el resultado sea el esperado

#dias= ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
#trabajadores = [11, 12, 5, 7, 9]

#NOTA las 2 listas no deben sufrir ningun cambio dentro de la funcion, se recomenda utilizar algun metodo para copiar
# el contenido que se quiere modificar.

# OUTPUT
#['Miércoles', 'Jueves', 'Viernes', 'Lunes', 'Martes']


#solucion

def ordenar(dias, trabajadores):
  lista3 = trabajadores.copy()
  lista3.sort()
  retornoDias = []
  for elemento in lista3:
    indice = trabajadores.index(elemento)
    retornoDias.append(dias[indice])
  return retornoDias

dias= ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
trabajadores = [11, 12, 5, 7, 9]


diasOrdenados = ordenar(dias,trabajadores)
print(diasOrdenados)