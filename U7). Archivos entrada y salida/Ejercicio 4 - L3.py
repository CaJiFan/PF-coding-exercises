#Terminado

#En una empresa le dan un documento .txt con los siguientes datos
#cliente,sucursal,mes,total
#datos:
#   Cliente: Nombre del cliente
#   Sucursal: Lugar
#   Mes: Numero del mes
#   Total: total de compra
#
#OBSERVE que el mes viene dado en numeros
# 1) Determine los clientes unicos que han comprado en las distintas sucursales de la empresa dentro de una lista
# 2) Determine el nombre del cliente que mas ha comprado en cada mes
#Output
#>>>{'Centro': ['Emilio', 'Luis', 'Kenya', 'Juan', 'Dan', 'Andres', 'Diego', 'Eduardo', 'Sebastian', 'Elena', 'Julia'], 'Sur': ['Emilio', 'Luis', 'Kenya', 'Juan', 'Dan', 'Andres', 'Diego', 'Eduardo', 'Sebastian', 'Elena', 'Julia'], 'Norte': ['Emilio', 'Luis', 'Kenya', 'Juan', 'Dan', 'Andres', 'Diego', 'Eduardo', 'Sebastian', 'Elena', 'Julia']}

#clientes que mas han comprado{'Marzo': 'Andres', 'Enero': 'Luis', 'Junio': 'Julia', 'Agosto': 'Emilio', 'Octubre': 'Luis', 'Septiempre': 'Dan', 'Julio': 'Luis', 'Febrero': 'Sebastian', 'Noviembre': 'Sebastian', 'Abril': 'Andres', 'Mayo': 'Andres', 'Diciembre': 'Emilio'}

lista_clientes = open('Eduardo Salavarria/7. Archivos/lista_clientes4.txt','r')
dict_sucursales = {}
for line in lista_clientes:
    cliente,sucursal,mes,total = line.strip().split(',')
    dict_sucursales[sucursal] = dict_sucursales.get(sucursal,[])
    dict_sucursales[sucursal].append(cliente)
    #no deben repetirse los clientes
    dict_sucursales[sucursal] = list(set(dict_sucursales[sucursal]))
print(dict_sucursales)
lista_clientes.close()

#determine cual es el cliente que MAS VECES ha comprado en cada mes
lista_clientes = open('Eduardo Salavarria/7. Archivos/lista_clientes4.txt','r')
dict_meses = {}
meses = ['Enero', 'Febrero', 'Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiempre','Octubre','Noviembre','Diciembre']
for line in lista_clientes:
    cliente,sucursal,mes,total = line.strip().split(',')
    mes, total = int(mes), float(total)
    mes_str = meses[mes-1]
    dict_meses[mes_str] = dict_meses.get(mes_str,[])
    dict_meses[mes_str].append(cliente)

for mes in list(dict_meses.keys()):
    clientes_unicos = list(set(dict_meses[mes]))
    conteo_cantidad = []
    for cliente in clientes_unicos:
        cantidad = dict_meses[mes].count(cliente)
        conteo_cantidad.append(cantidad)
    dict_meses[mes] = clientes_unicos[conteo_cantidad.index(max(conteo_cantidad))]
print(dict_meses) 