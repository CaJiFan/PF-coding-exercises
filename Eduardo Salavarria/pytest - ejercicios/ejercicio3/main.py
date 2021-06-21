#Terminado
#En un equipo de futbol se tiene una lista de jugadores con sus respectivas alturas y pesos de manera paralela realice las funciones requeridas en el archivo
#de funciones.py

from funciones import *
jugadores=["Carlos","Juan","Pedro","Luis","Marcos","José","Roberto","Eduardo", "Ramiro","Rubén","René", "Mario", "Jorge"]
altura = [180, 215, 210, 210, 188, 176, 209, 200, 210, 188, 176, 209, 200]
peso = [69, 74, 72, 75, 68, 70, 71, 73, 69, 74, 72, 75, 68, 70, 71, 73]
lista_imc = calcularimc(altura, peso)
print(lista_imc)
verificarJugadores(jugadores, lista_imc)
maxJugadores(jugadores, lista_imc)
calcularPromedio(lista_imc)