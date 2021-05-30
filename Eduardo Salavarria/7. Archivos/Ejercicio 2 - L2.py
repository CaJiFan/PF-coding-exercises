#determinar la cantidad de dinero que la empresa ha recibido en total
suma_total = 0.0
compras = open('Eduardo Salavarria/7. Archivos/palabras.txt','r')
for line in compras:
    cliente,compra = line.strip().split(',')
    compra = float(compra)
    suma_total += compra

print("La empresa ha recibido en total:",suma_total)  

#sacar el iva de cada una de las comprar y mostrar lo que cada persona ha comprado y al final el valor total recibido por la empresa
for line in compras:
    cliente,compra = line.strip().split(',')
    compra = float(compra)
    compra_iva = compra * 1.12
    print(f"El cliente {cliente} ha comprado ${compra} +IVA = ${compra_iva}")

import numpy as np
#determine el cliente que hizo la mayor compra en este mes
lista_clientes = []
lista_compras  = []
for line in compras:
    cliente,compra = line.strip().split(',')
    lista_clientes.append(cliente)
    lista_compras.append(float(compra))

array_compras = np.array(lista_compras)
array_clientes = np.array(lista_clientes)

cliente_mayor = array_compras[array_compras.argmax()]
compra_mayor = array_clientes[array_compras.argmax()]
print(f"El cliente que mas ha comprado en total es {cliente_mayor} con un total de {compra_mayor*1.14}")