restaurantes = ['KFC', 'Mc Donalds', 'La Esquina del Sabor', 'Menestras del Negro', 'Sweet and Coffee', 'Starbucks']
valoraciones = [4.4, 5, 3.2, 4.4, 5, 4.3]

#funcion en la que ingreses el nombre de un restaurante y te de su valoracion
def valoracion(restaurante, l_restaurante, l_valoraciones):
    index_pos = l_restaurante.index(restaurante)
    valoracion = l_valoraciones[index_pos]
    return valoracion


#funcion que determine el promedio de la lista
def promedio(l_valoraciones):
    promedio = sum(l_valoraciones)/len(l_valoraciones)
    return promedio

#con el uso de esa funcion muestre en pantalla los que estan arriba del promedio
def arribaPromedio(l_valoraciones, restaurantes):
    average = promedio(l_valoraciones)
    for index, valoracion in enumerate(l_valoraciones):
        if valoracion >= average:
            print(restaurantes[index], valoracion)

