#escriba un documento en orden de gasto por cada mes y en total
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