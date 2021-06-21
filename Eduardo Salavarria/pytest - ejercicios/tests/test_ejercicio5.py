#TEST TERMINADO
from ejercicio5.funciones import *

def test_suma():
    assert operacion("2+2") == (2, 2, "+")
def test_resta():
    assert operacion("2-2") == (2, 2, "-")
def test_multiplicacion():
    assert operacion("2*2") == (2, 2, "*")
def test_division():
    assert operacion("2/2") == (2,2,"/")

def test_operacion_suma():
    assert suma(2,1) == 3
def test_operacion_resta():
    assert resta(2,1) == 1
def test_operacion_multiplicacion():
    assert multiplicacion(2,4) == 8
def test_operacion_division():
    assert division(4,2) == 2

