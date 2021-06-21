#Terminado

#En una tienda los datos que le son proporcionados a usted son los codigos, precios y descuentos de cada uno de los productos que se encuentran en ella
#En la empresa le piden crear las siguientes funciones:
#1)Defina una funcion CalcularPrecio que nos va a ayudar a saber el precio de un producto solo teniendo el codigo del mismo. Los argumentos que recibe es el codigo del producto, el arreglo de los codigos de los productos de la tienda, el arreglo de los precios, y el descuento de cada uno de ellos. Retorne el precio del producto.

# 2)Defina una funcion CalcularTotal que recibe de argumentos una lista con los codigos de los objetos que se van a comprar en la tienda, el arreglo de los codigos de los productos de la tienda, el arreglo de los precios, y el descuento de cada uno de ellos. Esta funcion nos ayudara a calcular en total la suma total de los precios de los productos que se van a comprar. Retorne este valor.

import numpy as np
codigos = np.array(['001','002','003','004','005','006','007','008','009','010'])

precios = np.array([56.65, 32.00, 22.22, 100.93,23.45,78.56,90.90,34.67,89.34,450.89 ])

descuento = np.array([ 0, 12, 13, 7,35,50,75,0,10,30 ])



#Solucion

def calcularPrecio(codigo, C, P, D):
    precios = P - (P*(D/100))
    for i in C:
        if i == codigo:
            return precios[codigo==C]
        
        
def calcularTotal(codigos, C, P, D):
    codigosVector = np.array(codigos)
    precios = P - (P*(D/100)) 
    matrizValores = np.zeros(codigosVector.size)
    for i in range(codigosVector.size):  
        vectorBool = codigosVector[i] == C
        valor = precios[vectorBool] 
        
        matrizValores[i] = valor 
    return matrizValores.sum()

precioProducto = calcularPrecio('001', codigos, precios, descuento)
print(precioProducto)

listaCompras = calcularTotal(['001','002','003'], codigos, precios, descuento)
print(listaCompras)