#calculadora
def operacion(string):
    if "+" in string:
        signo = '+'
        n1,n2 = string.split("+")
        n1,n2 = float(n1), float(n2)
        return n1,n2,signo
    elif "-" in string:
        signo = '-'
        n1,n2 = string.split("-")
        n1,n2 = float(n1), float(n2)
        return n1,n2,signo
    elif "*" in string:
        signo = '*'
        n1,n2 = string.split("*")
        n1,n2 = float(n1), float(n2)
        return n1,n2,signo
    elif "/" in string:
        signo = '/'
        n1,n2 = string.split("/")
        n1,n2 = float(n1), float(n2)
        return n1,n2,signo

def suma(n1,n2):
    return n1 + n2

def resta(n1,n2):
    return n1-n2

def multiplicacion(n1,n2):
    return n1*n2

def division(n1,n2):
    if n2 == 0:
        print("Syntax Error")
    else:
        return n1/n2