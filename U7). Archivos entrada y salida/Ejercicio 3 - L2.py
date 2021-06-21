#Terminado

lista_clientes = open('Eduardo Salavarria/7. Archivos/lista_clientes.txt','r')

lista_clientes.readline()
meses = ['Enero', 'Febrero', 'Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiempre','Octubre','Noviembre','Diciembre']
#En una empresa a usted le dan los datos de las ventas que se han hecho, los datos estan puestos de la siguiente manera
#cliente,mes,cantidad
#Observe que el mes esta en numeros del 1-12
#La empresa le solicita lo siguiente

# 1) Cree un diccionario para saber las compras que han hechos los clientes en los diferentes meses
diccionario_mes = {}
for line in lista_clientes:
    cliente,mes,total = line.strip().split(',')
    
    mes = meses[int(mes)-1]
    diccionario_mes[mes] = diccionario_mes.get(mes, {})
    diccionario_mes[mes][cliente] = diccionario_mes[mes].get(cliente,[])
    diccionario_mes[mes][cliente].append(float(total))
print(diccionario_mes)


# 2) Cree un diccionario para saber cuanto se ha ganado en cada mes es total
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

# 3) Determine cual es el mes con mas ventas
mes_max = list(list_meses)[list(list_dinero).index(max(list(list_dinero)))]
print(f"El mes con mayor venta es {mes_max}")