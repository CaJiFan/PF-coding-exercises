#Dado el archivo "EDV 2016.csv", seleccione las	columnas:prov_insc,	edad_hom,	edad_muj y	mostremos
# los	primeros	20 registros usando Pandas



#OUTPUT
#     prov_insc  edad_hom  edad_muj  dur_mat
#0        Azuay        33        38       19
#1        Azuay        37        38       15
#2    Pichincha        39        49        0
#.....

#solucion
import pandas as pd


matrimonios= pd.read_csv("EDV 2016.csv",sep=';')
pareja = matrimonios[ ['prov_insc','edad_hom','edad_muj', 'dur_mat'] ]
print(pareja.head(20))