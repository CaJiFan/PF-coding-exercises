lista_clientes = open('Eduardo Salavarria/7. Archivos/lista_clientes.txt','r')
diccionario_mes = {}
lista_clientes.readline()
meses = ['Enero', 'Febrero', 'Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiempre','Octubre','Noviembre','Diciembre']
#diccionario para saber las compras que han hechos los clientes en los diferentes meses
for line in lista_clientes:
    cliente,mes,total = line.strip().split(',')
    
    mes = meses[int(mes)-1]
    diccionario_mes[mes] = diccionario_mes.get(mes, {})
    diccionario_mes[mes][cliente] = diccionario_mes[mes].get(cliente,[])
    diccionario_mes[mes][cliente].append(float(total))

#diccionario para saber cuanto se ha ganado en ese mes
print(diccionario_mes)
for mes in meses:
    clientes_mes = list(diccionario_mes[mes])
    for cliente in clientes_mes:
        diccionario_mes[mes][cliente] = sum(diccionario_mes[mes][cliente])
print(diccionario_mes)
for mes in meses:
    diccionario_mes[mes] = sum(list(diccionario_mes[mes].values()))
print(diccionario_mes)

list_meses = diccionario_mes.keys()
list_dinero = diccionario_mes.values()

mes_max = list(list_meses)[list(list_dinero).index(max(list(list_dinero)))]
print(f"El mes con mayor venta es {mes_max}")