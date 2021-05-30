def producto(codigo, l_precios, l_productos, l_codigos):
    indice = l_codigos.index(codigo)
    producto =  l_productos[indice]
    precio = l_precios[indice]
    return producto,precio


#defina una funcion que agregue productos en su bolsa
def addProducto(l_compras, l_bolsa):
    for producto in l_compras: 
        print(f"Se ha agregado {producto} a la lista de compras {l_bolsa} ")
        l_bolsa.append(producto)

#defina una funcion que determina el precio total de las compras
def precioTotal(l_compras, l_precios , l_productos , l_codigos):
    precio_total = 0
    for compra in l_compras:
        producto_compra, precio = producto(compra, l_precios, l_productos, l_codigos)
        precio_total += precio
        print(f"Se ha comprado {producto_compra} a {precio}" )
    print("Total a pagar", precio_total)
