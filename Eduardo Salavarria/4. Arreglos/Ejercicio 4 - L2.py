import numpy as np
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


codigos = np.array(['001','002','003','004','005','006','007','008','009','010'])

precios = np.array([56.65, 32.00, 22.22, 100.93,23.45,78.56,90.90,34.67,89.34,450.89 ])

descuento = np.array([ 0, 12, 13, 7,35,50,75,0,10,30 ])

precioProducto = calcularPrecio('001', codigos, precios, descuento)
print(precioProducto)

listaCompras = calcularTotal(['001','002','003'], codigos, precios, descuento)
print(listaCompras)