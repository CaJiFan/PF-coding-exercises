#Terminado

#En su programa genere dos listas con 10 numeros al lazar, elimine los repetidos en cada lista e imprima por pantalla los numeros que se repitan en los dos conjuntos

import numpy as np
from numpy.lib.arraysetops import union1d
array_l1 = np.random.randint(1,10,(10,), int)
array_l2 = np.random.randint(1,10,(10,), int)
l1 = array_l1.tolist()
l2 = array_l2.tolist()

l1_set = set(l1)
l2_set = set(l2)

union = l1_set & l2_set
if union == set():
    print("No hay ningun numero repetido")
else:
    print(union)
    print("Los numeros repetidos es/son: ")
    for numero in union:
        print(numero)