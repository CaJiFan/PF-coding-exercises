#Terminado

#En su programa se tiene los datos de restaurantes y valoraciones de los mismos en listas paralelas
#Se necesita de las siguientes funciones:
#1) Defina una funcion en la que ingrese el nombre de un restaurante y retorne su valoracion. De argumentos va a tener: el restaurante al cual se quiere saber su valoracion, la lista de restaurantes y la lista de las valoraciones.
#2) Defina una funcion que determine el promedio de las valoraciones de todos los restaurantes y lo retorne. Esta funcion debe tener como argumentos la lista de las valoraciones
#3) Defina una funcion que nos permita saber cuales son los restaurantes que se encuentran por encima del promedio. Esta funcion debe tener como argumento a la lista de las valoraciones y restaurantes


restaurantes = ['KFC', 'Mc Donalds', 'La Esquina del Sabor', 'Menestras del Negro', 'Sweet and Coffee', 'Starbucks']
valoraciones = [4.4, 5, 3.2, 4.4, 5, 4.3]

#Solucion
def valoracion(restaurante, l_restaurante, l_valoraciones):
    index_pos = l_restaurante.index(restaurante)
    valoracion = l_valoraciones[index_pos]
    return valoracion

def promedio(l_valoraciones):
    promedio = sum(l_valoraciones)/len(l_valoraciones)
    return promedio


def arribaPromedio(l_valoraciones, restaurantes):
    average = promedio(l_valoraciones)
    for index, valoracion in enumerate(l_valoraciones):
        if valoracion >= average:
            print(restaurantes[index], valoracion)

