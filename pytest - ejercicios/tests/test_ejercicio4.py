#TEST TERMIANDO
from ejercicio4.funciones import *
l_precios = [1,2.3,4.2,3,2]
l_productos = ['Cebolla', 'Papa', 'Queso', 'Pimiento', 'Pan']
l_codigos = ['001', '002', '003', '004', '005']
l_compras = ['001', '005']
l_bolsa = []

def test_producto():
    assert producto('001', l_precios, l_productos, l_codigos) == ('Cebolla', 1), 'El nombre del producto o el precio no es el correcto'

def test_precioTotal():
    assert precioTotal(l_compras,l_precios,l_productos,l_codigos) == 3, 'El total de la compra no es correcto'



