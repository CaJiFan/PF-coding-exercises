#Dadas las siguitentes listas defina 2 funciones que calculen lo siguiente:

#funcion edad(nombres,edades) devuelve una lista con el nombre de la persona de mayor edad y de menor edad
#funcion indiceMasa(nombres, peso, estatura) devuelve una lista con el nombre de la persona de mayor indice de masa
# corporal y el de menor, tenga en cuenta que el indice de masa corporal se calcula con IMC = peso(KG) / (alturna(m))^2


# al final probar las 2 funciones y mostrar por pantalla las listas

#nombres = ["dominguez","paredes","achilier","erazo, “valencia"]
#peso = [78.56,90.65,80.76,57.30, 90.35]
#edades = [23,22,25,26, 28]
#estatura = [1.89,1.77,1.80,1.75, 1.85]

#NOTA: las listas no deben sufrir ningun cambio dentro de la funcion.

# OUTPUT:
#FUNCION 1
#['valencia', 'paredes']
#FUNCION 2
#['paredes', 'erazo']


#solucion

def edad(nombres, edades):
  indMax = edades.index(max(edades))
  indMin = edades.index(min(edades))
  return [nombres[indMax], nombres[indMin]]

def indiceMasa(nombres, peso, estatura):
  masas = []
  for ind in range(len(nombres)):
    masas.append(peso[ind]/(estatura[ind]**2))
  indMax = masas.index(max(masas))
  indMin = masas.index(min(masas))
  return [nombres[indMax], nombres[indMin]]



nombres = ["dominguez","paredes","achilier","erazo", "valencia"]
peso = [78.56,90.65,80.76,57.30,90.35]
edades = [23,22,25,26,28]
estatura = [1.89,1.77,1.80,1.75,1.85]

print("FUNCION 1")
print(edad(nombres,edades))

print("FUNCION 2")
print(indiceMasa(nombres, peso, estatura))