#Dado el archivo "EDV 2016.csv", muestre por pantalla las respuestas de:
#¿Cuánto	es	el	promedio	de	los	años	de	inscripción?
#¿Cuál	es	el	promedio	de	los	años	de	divorcio?
#¿Cuál	es	el	mínimo	y	máximo	del	año	de	matrimonio?


#OUTPUT

#Promedio años de inscripcion:  2016.0
#Promedio años de divorcio:  2015.5660480349345
#Minino:  1946
#Máximo:  2016

#solucion
import pandas as pd


matrimonios= pd.read_csv("EDV 2016.csv",sep=';')
df = matrimonios['anio_insc'].mean()
print("Promedio años de inscripcion: ", df)
df2 = matrimonios['anio_div'].mean()
print("Promedio años de divorcio: ",df2)
dfmin = matrimonios['anio_mat'].min()
print("Minino: ", dfmin)
dfmax = matrimonios['anio_mat'].max()
print("Máximo: ", dfmax)