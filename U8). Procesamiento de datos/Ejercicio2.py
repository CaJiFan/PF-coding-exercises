#Dado el archivo "EDV 2016.csv", agrupe	 el	DataFrame	 de	 matrimonios por
# prov_ins	 y	 cuente	 sus	 ocurrencias


#OUTPUT
#prov_insc
#Azuay                             1982
#Bol?var                            320
#Ca?ar                              782
#Carchi                             317
#Chimborazo                         963
#.....

#solucion
import pandas as pd


matrimonios= pd.read_csv("EDV 2016.csv",sep=';')
pareja = matrimonios[ ['prov_insc'] ]
matrimonios_group = pareja.groupby('prov_insc')
print( matrimonios_group.size() )