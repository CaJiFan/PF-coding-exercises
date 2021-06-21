#Terminado

#Usted trabaja en una tienda y le piden definir las funciones que se encuentran en el archivo "funciones.py" los datos de la tienda que le son proporcionados son una lista con los precios de los productos, lista de los nombres de los productos y una lista con los codigos de cada uno de los productos

from funciones import *
l_precios = [1,2.3,4.2,3,2]
l_productos = ['Cebolla', 'Papa', 'Queso', 'Pimiento', 'Pan']
l_codigos = ['001', '002', '003', '004', '005']

#defina una funcion que pueda ingresar un codigo y retorne el nombre del producto y el precio
l_compras = ['001', '005', '003', '002']

producto,precio=producto('001', l_precios, l_productos, l_codigos)
print(producto,precio)
print(producto, precio)
precioTotal(l_compras, l_precios , l_productos , l_codigos)