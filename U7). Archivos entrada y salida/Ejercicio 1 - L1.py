#Terminado

#En una tienda se guardan los datos dentro de un archivo .txt 
#Se tiene de datos el nombre del cliente y la compra que ha realizado de la siguiente forma
#cliente,compra
#Muestre en pantalla las personas que han comprado y el total de la compra realizada

compras = open('Eduardo Salavarria/7. Archivos/ventas.txt','r')
compras.readline()
lista_clientes = []
for line in compras:
    cliente,compra = line.strip().split(',')
    print(f"El cliente {cliente} ha comprado ${float(compra)} en total")
    lista_clientes.append(cliente)
