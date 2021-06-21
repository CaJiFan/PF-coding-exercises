#Terminado

#En una empresa se le entregan los datos de:
#cliente, cantidad
#cliente: Nombre del cliente
#Cantidad: Cantidad comprada por el cliente
#Se le pide a usted como programador los siguientes datos que se necesitan:
#1) Determinar la cantidad de dinero que la empresa ha recibido en total
#2) Aumente el iva de cada una de las compras y mostrar lo que cada persona ha comprado en la tienda
#3) Determinar el cliente que hizo la mayor compra

suma_total = 0.0
compras = open('Eduardo Salavarria/7. Archivos/ventas.txt','r')
#1) Determinar la cantidad de dinero que la empresa ha recibido en total
for line in compras:
    cliente,compra = line.strip().split(',')
    compra = float(compra)
    suma_total += compra

print("La empresa ha recibido en total:",suma_total)  

#2) Aumente el iva de cada una de las compras y mostrar lo que cada persona ha comprado en la tienda
#>>> El cliente Pedro ha comprado $10 + IVA = $11.2
for line in compras:
    cliente,compra = line.strip().split(',')
    compra = float(compra)
    compra_iva = compra * 1.12
    print(f"El cliente {cliente} ha comprado ${compra} +IVA = ${compra_iva}")

import numpy as np

#3) Determinar el cliente que hizo la mayor compra
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
compras.close()