#muestre en pantalla las personas con la compra que han hecho
compras = open('Eduardo Salavarria/7. Archivos/palabras.txt','r')
compras.readline()
lista_clientes = []
for line in compras:
    cliente,compra = line.strip().split(',')
    print(f"El cliente {cliente} ha comprado ${float(compra)} en total")
    lista_clientes.append(cliente)
print(lista_clientes)