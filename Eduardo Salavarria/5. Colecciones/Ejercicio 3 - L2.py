#Terminado

nombres = ['Radman Erdmann', 'Kirit Bonnette', 'Heddwyn Sheahan', 'Fitzjames Cortese', 'Sesto Sacks', 'Farnley Erdmann', 'Dheran Alban', 'Garvey Ealy', 'Mahabala Bland', 'Gamaliel Bowens', 'Richard Sheahan', 'Sadik Huerta', 'Bedrich Ort', 'Hargreave Nevins', 'Angwyn Doctor', 'Kaushik Ketterer', 'Teulyddog Kenyon', 'Tristan Chalker', 'Vasu Nakano', 'Troilus Pack', 'Devin Zeitler', 'Jamie Mcdermott', 'Thies Veras', 'Orton Rubinstein', 'Giovanni Ficklin', 'Chaika Heeter', 'Carlton Calhoun', 'SeÃ±or Wheeler', 'Maynard Kester', 'Suvrata Bragdon', 'Nathaniel Hardiman', 'Nabendu Ernst', 'Lundy Zeitler', 'Tristan Montesdeoca', 'Dharuna Bechtold', 'Nevin Connelly', 'Dharuna Loo', 'Coalan Paulin', 'Kerry Hutcheson', 'Ravi Zeitler', 'Enrico Stanger', 'Orban Islas', 'Pranay Silvis', 'Dheran Berryhill', 'Iorweth Sweeny', 'Murphy Hardiman', 'Akiyama Cortese', 'Chiranjeev Reinhardt', 'Lel Riojas', 'Gordon Montesdeoca']

ingreso_years = [2019, 2020, 2018, 2017, 2018, 2020, 2021, 2017, 2021, 2021, 2021, 2019, 2017, 2017, 2019, 2018, 2017, 2019, 2021, 2018, 2017, 2020, 2018, 2020, 2021, 2019, 2019, 2019, 2019, 2019, 2017, 2019, 2021, 2018, 2019, 2021, 2021, 2020, 2018, 2021, 2017, 2018, 2018, 2019, 2017, 2021, 2017, 2018, 2019, 2018] 

#Defina la funcion registroYear que nos permita saber los estudiantes que fueron registrados en un año determinado. Esta funcion recibe de argumentos el año ingresado por el usuario, la lista de años de los estudianes ya registrados asi mismo como una lista de los nombres de los estudiantes

def registroYear(year, years, names):
    nombres_estudiantes = names[years==year]
    print(f"Los estudiantes que fueron registrados el año {year} fueron: ")
    for nombre in nombres_estudiantes:
        print(nombre)



#Defina una funcion dict_year que cree un diccionario y que ordene como clave el año y el valor una lista de los nombres de los estudiantes que fueron registrados en ese año. Los argumentos que recibe esta funcion son: diccionario, la lista de nombres, y la lista de los años en la que los estudiantes fueron registrados.

#EJEMPLO
# {2019: ['Radman Erdmann', 'Sadik Huerta', 'Angwyn Doctor', 'Tristan Chalker', 'Chaika Heeter', 'Carlton Calhoun', 'SeÃ±or Wheeler', 'Maynard Kester', 'Suvrata Bragdon', 'Nabendu Ernst', 'Dharuna Bechtold', 'Dheran Berryhill', 'Lel Riojas'], 2020: ['Kirit Bonnette', 'Farnley Erdmann', 'Jamie Mcdermott', 'Orton Rubinstein', 'Coalan Paulin'], 2018: [...]}

def dict_year(diccionario, nombres, ingreso_years):
    for index,year in enumerate(ingreso_years):
        nombre = nombres[index]
        diccionario[year] = diccionario.get(year, [])
        diccionario[year].append(nombre)
    print(diccionario)

diccionario = {}
dict_year(diccionario, nombres, ingreso_years)


#Dentro del programa principal y con la ayuda del diccionario determine una manera de saber cual fue el año en el que se registraron mas estudiantes

years = list(diccionario.keys())
count_years = []
for year in years:
    cantidad = len(diccionario[year])
    count_years.append(cantidad)
indice_max = count_years.index(max(count_years))
print(f"El año que hubo mas estudiantes fue {years[indice_max]} con {count_years[indice_max]} estudiantes.")
    



    

