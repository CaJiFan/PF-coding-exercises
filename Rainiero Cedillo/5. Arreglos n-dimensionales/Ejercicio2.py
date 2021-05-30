#Dada una ciudad y un tipo de gasolinera encuentre su total de ventas de galones. Cree una funcnion que reciba
# la ciudad pedida, la lista de ciudades, el tipo de gasolina y la lista de tipos de gasolina con la matriz,.
# Retorne el total de ventas para esa ciudad y tipo de gasolina dado.

#Utilice los siguientes datos
#tipoGasolina	=	['Regular',	'Extra',	'Súper',	'Diesel',	'Ecopais',	'Premium']
#gasolineras	=	['Primax	Alborada',	'Mas	Gas	Alborada',	'PetroComercial','PetrolRios',	'PetrolRios',	'PS	Los	Ríos',	'Mobil	Cumbayá',	'PDV	sa	Los	Chillos','Lutexsa CIA	Ltda','PS	Remigio	Crespo']
#ciudades	=	['Guayaquil',	'Guayaquil',	'Guayaquil',		'Babahoyo', 	'Cuenca',    'Babahoyo',				'Quito'	,					'Quito'	,	'Guayaquil',	'Quito']
#M	=	np.random.randint(4000,1500000,	size=(len(tipoGasolina),len(gasolineras)))

# NOTA: Las filas son los tipos de gasolina y las columnas de la matriz son el nombre de las gasolineras


#solucion
import numpy as np
tipoGasolina	=	['Regular',	'Extra',	'Súper',	'Diesel',	'Ecopais',	'Premium']
gasolineras	=	['Primax	Alborada',	'Mas	Gas	Alborada',	'PetroComercial','PetrolRios',	'PetrolRios',	'PS	Los	Ríos',	'Mobil	Cumbayá',	'PDV	sa	Los	Chillos','Lutexsa CIA	Ltda','PS	Remigio	Crespo']
ciudades	=	['Guayaquil',	'Guayaquil',	'Guayaquil',		'Babahoyo', 	'Cuenca',    'Babahoyo',				'Quito'	,					'Quito'	,	'Guayaquil',	'Quito']
M	=	np.random.randint(4000,1500000,	size=(len(tipoGasolina),len(gasolineras)))


def total_galones(ciudad,lista_ciudades,gasolina,tipos_gasolinas,matriz):
  columnas =[]
  for a in range(len(lista_ciudades)):
      if ciudades[a] == ciudad:
          columnas.append(a)
  fila = tipos_gasolinas.index(gasolina)
  lista= []
  for i in columnas:
      lista.append(matriz[fila,i])
  matriz2 = np.array(lista,int)
  total= matriz2.sum()
  return total