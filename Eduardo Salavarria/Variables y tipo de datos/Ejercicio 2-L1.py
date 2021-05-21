#En una carretera el limite de velocidad es 70km/h y se pondra multa a las personas que sobrepasen el limite de velocidad.
#Por lo que para mantener un correcto transito en la via se necesita calular las velocidades de los autos.
#Lamentablemente los datos que se obtienen son la distancia (120 METROS) y un tiempo recorrido
#realice un programa que nos ayude a saber si el conductor sobrepaso los limites de velocidad y si tiene multa o no.
#Ejemplo: 

#Tiene multa: True

#Tambien muestre en pantalla la velocidad en km/h que tenia el vehiculo

#Nota: velocidad = metros / segundos


#conductor_1  recorrio 120 metros en 2.99 segundos

limite_velocidad = 70
distancia = 120
tiempo = 2.99

velocidad_ms = distancia/tiempo
velocidad_kms = velocidad_ms*(18/5)

sobrepaso = velocidad_kms >= limite_velocidad

print("La velocidad que tiene el vehiculo en m/s:", velocidad_ms)
print("La velocidad que tiene el vehiculo en Km/h:", velocidad_kms)
print("Sobrepaso los limites de velocidad?:", sobrepaso)

