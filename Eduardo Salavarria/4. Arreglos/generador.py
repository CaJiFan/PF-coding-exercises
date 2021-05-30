import random as rd

compras = []
sucursales = ['Norte','Sur','Centro']
clientes = ['Sebastian', 'Luis', 'Kenya', 'Juan', 'Andres', 'Dan', 'Julia', 'Emilio', 'Eduardo', 'Elena', 'Diego']
for i in range(200):
    numero = rd.randint(10,1000)
    mes = rd.randint(1,12)
    cantidad = float(numero) + (float(numero)/121)
    compra = round(cantidad,2)
    cliente = rd.choice(clientes)
    sucursal = rd.choice(sucursales)
    print(f"{cliente},{sucursal},{mes},{compra}")

