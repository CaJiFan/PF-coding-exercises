#Terminado

#Con la misma dinamica de los ejercicios anteriores la empresa le entrega a usted los siguientes datos en un documento .txt
#Cliente,Sucursal,Mes,Total
#Cliente: Nombre del Cliente
#Sucursal: Lugar donde fue hecha la compra
#Mes: Numero del mes en que fue hecha la compra
#Total: Total hecho de la compra

#1) Cree un diccionario que tenga como CLAVE el mes de la compras realizadas y como valor una lista con tuplas en la que se incluyen
#los nombres y el total de la compra hecha. Esta lista de tuplas debe estar ORDENADA de mayor a menor de la siguiente manera:
#Output
#>>>
# {'Marzo': [('Andres', 1803.79), ('Julia', 1228.06), ('Sebastian', 1017.3399999999999), ('Elena', 889.29), ('Emilio', 734.01), 
# ('Eduardo', 355.91999999999996), ('Luis', 228.88), ('Diego', 24.2)], 'Enero': [('Julia', 1333.93), ('Dan', 1218.99), ('Elena', 
# 1090.94), ('Eduardo', 1071.79), ('Sebastian', 817.7), ('Kenya', 718.89), ('Juan', 711.83), ('Emilio', 709.82), ('Diego', 626.14),
#  ('Luis', 265.18)], 'Junio': [('Eduardo', 1767.49), ('Luis', 1505.3400000000001), ('Julia', 1240.17), ('Elena', 1194.8), 
# ('Sebastian', 1154.47), ('Emilio', 962.89), ('Andres', 873.16), ('Kenya', 673.52), ('Diego', 197.62)], 'Agosto': [('Emilio', 1781.
# 61), ('Andres', 1763.45), ('Dan', 1636.4099999999999), ('Elena', 939.7), ('Kenya', 841.9), ('Julia', 742.08), ('Juan', 740.07), 
# ('Luis', 362.98), ('Eduardo', 351.88)], 'Octubre': [...]}


#2) Cree un documento que tenga de nombre MesesTotales.txt en el que va a escribir los meses en orden (Ene-Dic) y las compras de mayor
#a menor de la siguiente manera:
#Enero,Julia,1333.93
# Enero,Dan,1218.99
# Enero,Elena,1090.94
# Enero,Eduardo,1071.79
# Enero,Sebastian,817.7
# Febrero,Julia,2709.2000000000003
# Febrero,Diego,1775.5500000000002
# Febrero,Elena,588.83
# Febrero,Dan,120.99
# Marzo,Eduardo,355.91999999999996
# Marzo,Luis,228.88
# Marzo,Diego,24.2
# Abril,Diego,1593.06
# Abril,Emilio,1512.39
# Abril,Elena,915.5
# Abril,Sebastian,908.44

# 3)Determine la venta total del año en la empresa
lista_clientes = open('Eduardo Salavarria/7. Archivos/lista_clientes4.txt','r')
meses = ['Enero', 'Febrero', 'Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiempre','Octubre','Noviembre','Diciembre']

diccionario_mes = {}
for line in lista_clientes:
    cliente,sucursal,mes,total = line.strip().split(',')
    
    mes = meses[int(mes)-1]
    diccionario_mes[mes] = diccionario_mes.get(mes, {})
    diccionario_mes[mes][cliente] = diccionario_mes[mes].get(cliente,[])
    diccionario_mes[mes][cliente].append(float(total))

for mes in list(diccionario_mes.keys()):
    clientes_mes = list(diccionario_mes[mes])
    for cliente in clientes_mes:
        diccionario_mes[mes][cliente] = sum(diccionario_mes[mes][cliente])

import numpy as np
for mes in list(diccionario_mes.keys()):
    diccionario_mes[mes] = list(diccionario_mes[mes].items())
    lista_nombres = []
    lista_totales = []
    for dato in diccionario_mes[mes]:
        nombre,total = dato
        lista_nombres.append(nombre)
        lista_totales.append(total)
    array_nombres = np.array(lista_nombres)
    array_totales = np.array(lista_totales)
    indices_ordenados = array_totales.argsort()[::-1]
    lista_nombres1 = array_nombres[indices_ordenados].tolist()
    lista_totales1 = array_totales[indices_ordenados].tolist()
    lista_tuplas = []
    for indice, total in enumerate(lista_totales1):
        nombre = lista_nombres1[indice]
        tupla_generatriz = (nombre,total)
        lista_tuplas.append(tupla_generatriz)
    diccionario_mes[mes] = lista_tuplas
    
print(diccionario_mes)

documento = open('Eduardo Salavarria/7. Archivos/MesesTotales.txt','w')
for mes in meses:    
    if mes in list(diccionario_mes.keys()):
        lista_tupla = diccionario_mes[mes]
        for nombreTotal in lista_tupla:
            nombre,total = nombreTotal
            line = mes +','+ nombre +',' + str(total) +'\n'
            documento.write(line)
documento.close()
total_year = 0
documento = open('Eduardo Salavarria/7. Archivos/MesesTotales.txt','r')
for line in documento:
    mes,nombre,total = line.strip().split(',')
    total_year += float(total)
print("El total de año se ha vendido", total_year)