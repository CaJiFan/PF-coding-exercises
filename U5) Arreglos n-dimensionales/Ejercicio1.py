#Crear una función que reciba la lista de precios y mediante numpy les calcule el iva. La función debe retornar un
# arreglo de numpy con los precios incluidos el iva (12%).
#NOTA: el arreglo ingresado no debe modificarse. No importa el redondeo de los resultados




#solucion
import numpy as np

def funcionIva (precios):
  iva = np.array([precios])
  H = iva+(iva*(0.12))
  Iva = H
  return Iva


precios = [0.14, 2.18, 8.23, 5.00, 75.12, 94.12, 1.51, 45.00, 32.22]
print(funcionIva(precios))