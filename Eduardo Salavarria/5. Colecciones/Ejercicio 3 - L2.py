import numpy as np
#defina una funcion que registre los datos del estudiante
#nombre y año de ingreso
#retorne una tupla

nombres = ['Radman Erdmann', 'Kirit Bonnette', 'Heddwyn Sheahan', 'Fitzjames Cortese', 'Sesto Sacks', 'Farnley Erdmann', 'Dheran Alban', 'Garvey Ealy', 'Mahabala Bland', 'Gamaliel Bowens', 'Richard Sheahan', 'Sadik Huerta', 'Bedrich Ort', 'Hargreave Nevins', 'Angwyn Doctor', 'Kaushik Ketterer', 'Teulyddog Kenyon', 'Tristan Chalker', 'Vasu Nakano', 'Troilus Pack', 'Devin Zeitler', 'Jamie Mcdermott', 'Thies Veras', 'Orton Rubinstein', 'Giovanni Ficklin', 'Chaika Heeter', 'Carlton Calhoun', 'SeÃ±or Wheeler', 'Maynard Kester', 'Suvrata Bragdon', 'Nathaniel Hardiman', 'Nabendu Ernst', 'Lundy Zeitler', 'Tristan Montesdeoca', 'Dharuna Bechtold', 'Nevin Connelly', 'Dharuna Loo', 'Coalan Paulin', 'Kerry Hutcheson', 'Ravi Zeitler', 'Enrico Stanger', 'Orban Islas', 'Pranay Silvis', 'Dheran Berryhill', 'Iorweth Sweeny', 'Murphy Hardiman', 'Akiyama Cortese', 'Chiranjeev Reinhardt', 'Lel Riojas', 'Gordon Montesdeoca']

ingreso_years = [2019, 2020, 2018, 2017, 2018, 2020, 2021, 2017, 2021, 2021, 2021, 2019, 2017, 2017, 2019, 2018, 2017, 2019, 2021, 2018, 2017, 2020, 2018, 2020, 2021, 2019, 2019, 2019, 2019, 2019, 2017, 2019, 2021, 2018, 2019, 2021, 2021, 2020, 2018, 2021, 2017, 2018, 2018, 2019, 2017, 2021, 2017, 2018, 2019, 2018] 


#defina una funcion que solicite un añp al usuario e imprima a todos los estudiantes que fueron registrados en ese año
def registroYear(year, years, names):
    nombres_estudiantes = names[years==year]
    print(f"Los estudiantes que fueron registrados el año {year} fueron: ")
    for nombre in nombres_estudiantes:
        print(nombre)

#defina funcion que cree un diccionario y tenga como clave el año y de valor una lista
def dict_year(diccionario, nombres, ingreso_years):
    for index,year in enumerate(ingreso_years):
        nombre = nombres[index]
        diccionario[year] = diccionario.get(year, [])
        diccionario[year].append(nombre)
    print(diccionario)

diccionario = {}
#determine cual es el año que tuvo mas estudiantes
years = list(diccionario.keys())
count_years = []
for year in years:
    cantidad = len(diccionario[year])
    count_years.append(cantidad)
indice_max = count_years.index(max(count_years))
print(f"El año que hubo mas estudiantes fue {year[indice_max]} con {count_years[indice_max]} estudiantes.")
    



    

