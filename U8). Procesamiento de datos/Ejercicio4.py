#Dado el archivo "EDV 2016.csv", obtenga	los	 datos	 estadísticos	 de	las	 columnas: 'edad_hom','edad_muj', 'dur_mat'


#OUTPUT

#Columna edad_hom
#count    25648.000000
#mean        42.106363
#std         12.937366
#min         18.000000
#25%         33.000000
#50%         41.000000
#75%         49.000000
#max        999.000000
#Name: edad_hom, dtype: float64
#
#Columna edad_muj
#count    25648.000000
#mean        39.083047
#......


#solucion
import pandas as pd


matrimonios= pd.read_csv("EDV 2016.csv",sep=';')
df = matrimonios['edad_hom']. describe()
print("Columna edad_hom")
print(df)
df1 = matrimonios['edad_muj']. describe()
print("\nColumna edad_muj")
print(df1)
df2 = matrimonios['dur_mat']. describe()
print("\nColumna dur_mat")
print(df2)