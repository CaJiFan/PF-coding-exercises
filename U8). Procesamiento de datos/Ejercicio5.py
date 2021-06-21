#Dado el archivo "EDV 2016.csv", muestre por pantalla las respuestas de:
#¿Qué	tipo	de	dato	es	la	provincia	inscrita?
#¿Qué	tipo	de	dato	es la	edad	del	hombre?
#¿Qué	tipo	de	dato	es	la	duracion del matrimonio?



#OUTPUT

#Provincia   inscrita : object
#Edad    del hombre:  int64
#Duracion del matrimonio:  int64


#solucion
import pandas as pd


matrimonios= pd.read_csv("EDV 2016.csv",sep=';')
print("Provincia	inscrita :", matrimonios['prov_insc'].dtypes)
print("Edad	del	hombre: ", matrimonios['edad_hom'].dtypes)
print("Duracion del matrimonio: ", matrimonios['dur_mat'].dtypes)