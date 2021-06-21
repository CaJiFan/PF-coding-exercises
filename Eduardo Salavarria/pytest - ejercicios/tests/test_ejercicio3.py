#tEST TERMINADO
from ejercicio3.funciones import *
jugadores=["Carlos","Juan","Pedro","Luis","Marcos","José","Roberto","Eduardo", "Ramiro","Rubén","René", "Mario", "Jorge"]
l_altura = [180, 215, 210, 210, 188, 176, 209, 200, 210, 188, 176, 209, 200]
l_peso = [69, 74, 72, 75, 68, 70, 71, 73, 69, 74, 72, 75, 68, 70, 71, 73]
imc_jugadores = [21.3, 16.01, 16.33, 17.01, 19.24, 22.6, 16.25, 18.25, 15.65, 20.94, 23.24, 17.17, 17.0]

def test_calcular_imc():
    
    assert calcularimc(l_altura,l_peso) == imc_jugadores, 'Estas calculando mal el IMC de los jugadores.'

def test_verificarJugadores():
    assert verificarJugadores(['Rene','Jose','Eduardo'], [17.5, 18, 19]) == ['Rene'], 'Estas incluyendo mal los jugadores que tienen el IMC menor.'


def test_maxJugadores():
    assert maxJugadores(['Eduardo','Juan','Daniel'],[10,10,2]) == ['Eduardo','Juan'], 'No se encuentran todos los jugadores'
    assert maxJugadores(['Eduardo', 'Juan','Daniel'],[10,9,8]) == ['Eduardo'], 'Los jugadores con mayor IMC no son los correcto'

def test_calcularPromedio():
    assert calcularPromedio([5,5,5,5]) == 5, 'Equivocacion en la forma de sacar el promedio.'