juegos = ['001-A','002-B', '003-C', '004-D', '005-E', '006-F']
categorias = ['Terror','Psicologico','Shooter','Terror','Shooter','Shooter']
plataformas = ['SWITCH','PS4','PS4', 'PC','XBOX','PCP']

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