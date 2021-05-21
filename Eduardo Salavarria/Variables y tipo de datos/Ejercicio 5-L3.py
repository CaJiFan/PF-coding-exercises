#Borrador
#recTech una compañia de videojuegos le pide a usted que le realice un programa con el que se pueda jugar a el famoso juego de el ahorcado para ello le da un texto(inmutable) con las palabras necesarias para el juego (las primera dos palabras y las dos ultimas)
#el juego consiste en poner una palabra al azar y mostrarla de la siguiente manera
#Ejemplo:
#
#       N _ _ _ _ E =  nombre
#
#Luego, pida al usuario que ingrese una palabra y verfique con True o False si la palabra que ingreso es correcta.

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
chosen_word = lista_palabras[random_index]
first_char = chosen_word[0]
last_char = chosen_word[-1]
print(first_char+(" _ "*(len(chosen_word)-2))+last_char)

palabra_usuario = input("Ingrese una palabra: ")
print("La palabra es correcta?", palabra_usuario==chosen_word)