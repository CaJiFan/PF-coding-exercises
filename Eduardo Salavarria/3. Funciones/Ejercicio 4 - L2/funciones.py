#Solucion
#Defina una funcion producto que tenga como argumentos el codigo requerido por el usuario codigo, la lista de precios, lista de productos, lista de codigos y retorne el nombre del producto y el precio del mismo.
def producto(codigo, l_precios, l_productos, l_codigos):
    indice = l_codigos.index(codigo)
    producto =  l_productos[indice]
    precio = l_precios[indice]
    return producto,precio


#Defina una funcion que agregue productos en su bolsa los argumentos que recibe es una lista de compras y la bolsa en que va a llevar los productos de la tienda

def addProducto(l_compras, l_bolsa):
    for producto in l_compras: 
        print(f"Se ha agregado {producto} a la lista de compras {l_bolsa} ")
        l_bolsa.append(producto)

#Defina una funcion que determina el precio total de las compras
def precioTotal(l_compras, l_precios , l_productos , l_codigos):
    precio_total = 0
    for compra in l_compras:
        producto_compra, precio = producto(compra, l_precios, l_productos, l_codigos)
        precio_total += precio
        print(f"Se ha comprado {producto_compra} a {precio}" )
    print("Total a pagar", precio_total)
