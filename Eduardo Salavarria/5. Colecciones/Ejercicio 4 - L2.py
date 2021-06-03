#Terminado

#En un programa de python se le da los datos de una lista de juegos con sus respectivos codigos de venta, una lista de categorias de los juegos
#y las plataformas (cada una es paralela a la otra).
#En su programa se le pide crear un diccionario de categorias que ordene cada uno de los juegos por su categoria; teniendo como CLAVE
#la categoria y como VALOR una lista de los juegos que pertenecen a esa categoria.
#Tambien se solicita crear un diccionario de las plataformas en las que se puede jugar estos videojuegos.
#Ejemplo
#   {'Terror': ['001-A', '004-D'], 'Psicologico': ['002-B'], 'Shooter': ['003-C', '005-E', '006-F']}
#   {'SWITCH': ['001-A'], 'PS4': ['002-B', '003-C'], 'PC': ['004-D'], 'XBOX': ['005-E'], 'PCP': ['006-F']}

#Solucion
juegos = ['001-A','002-B', '003-C', '004-D', '005-E', '006-F']
categorias = ['Terror','Psicologico','Shooter','Terror','Shooter','Shooter']
plataformas = ['SWITCH','PS4','PS4', 'PC','XBOX','PC']

dict_categorias = {}
for index, categoria in enumerate(categorias):
    dict_categorias[categoria] = dict_categorias.get(categoria, [])
    juego = juegos[index]
    dict_categorias[categoria].append(juego)

dict_plataformas = {}

for index, plataforma in enumerate(plataformas):
    dict_plataformas[plataforma] = dict_plataformas.get(plataforma,[])
    juego = juegos[index]
    dict_plataformas[plataforma].append(juego)

print(dict_categorias)
print(dict_plataformas)