#Terminado

#Una compañía de videojuegos le pide a usted desarrollar el juego del ahorcado, el CEO de la empresa deja una conversación en la que detalla que palabras quiere que sean utilizadas. 
#En su programa debe crear una manera conveniente de poder determinar estas palabras y escoger una al azar.
#También para poder crear el juego uno de los requisitos indispensables es poder mostrar la primera y la ultima letra de la palabra (en mayúsculas).
#Ejemplo:
#
#       N _ _ _ _ E =  nombre
#
#Luego, pida al usuario ingresar una palabra para verificar si es la correcta y que muestre en pantalla True si la palabra es la misma que el programa eligió al azar y False si la palabra que ingresó esta incorrecta.


import random as rd

texto = "Las palabras para que utilices en el videojuego son: #reconocer y #perfume pero no quiero que pongas la palabra #ojo es muy corta, pero estas de aqui sí: #mueble y #computadora"

index_palabra1_ini = texto.index('#') + 1
index_palabra1_fin = texto.index(' ', index_palabra1_ini+1)

index_palabra2_ini = texto.index("#", index_palabra1_ini + 1) + 1
index_palabra2_fin = texto.index(" ", index_palabra2_ini + 1)


texto_inv = texto[::-1]
index_palabra3_ini = texto_inv.index("#") 

index_palabra4_ini = texto_inv.index("#", index_palabra3_ini+1)

palabra_1 = texto[index_palabra1_ini:index_palabra1_fin]
palabra_2 = texto[index_palabra2_ini:index_palabra2_fin]
palabra_3 = texto_inv[:index_palabra3_ini][::-1]

palabra_4 = texto_inv[:index_palabra4_ini][::-1]
index_palabra4_fin = palabra_4.index(" ")
palabra_4 = palabra_4[:index_palabra4_fin]

lista_palabras = [palabra_1,palabra_2,palabra_3,palabra_4]

random_index = rd.randrange(len(lista_palabras))
chosen_word = lista_palabras[random_index].upper()
first_char = chosen_word[0]
last_char = chosen_word[-1]
print(first_char+(" _ "*(len(chosen_word)-2))+last_char)

palabra_usuario = input("Ingrese una palabra: ").upper()
print("La palabra es correcta?", palabra_usuario==chosen_word)