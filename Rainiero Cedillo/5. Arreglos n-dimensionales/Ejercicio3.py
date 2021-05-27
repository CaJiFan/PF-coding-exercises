#Encuentre el total de gasolineras cuyas ventas es mayor al promedio de ventas para un tipo de Gasolina dado.
# Cree una función que reciba el tipo de gasolina a buscar, el listado de tipos de gasolina y la matriz.
# Retorne el total de gasolineras

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


def GasolinerasMas(gasolina,tipos_gasolinas,matriz):
  fila = tipos_gasolinas.index(gasolina)
  promedioGeneral = matriz.mean(axis=1)
  maximo = promedioGeneral[fila]
  matriz2 = matriz.copy()
  valores = matriz2[fila][:] > maximo
  cantidad = valores.sum()
  return cantidad