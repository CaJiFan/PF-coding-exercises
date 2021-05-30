#Dado una conjunto de x con números enteros, escriba una función para contar sus
#elementos pares e impares. La función retornara 2 conjuntos, conjunto de pares y
#conjunto de impares. Mostrar por pantalla los resultados


#Ejemplo
#x={23, 45, 76, 84, 91, 52}
#Output
#{76,84,52}, {23,45,91}

#Solucion
def contar(x):
    lista = list(x)
    pares = []
    impares = []
    for a in range(len(lista)):
        if lista[a]%2 == 0:
            pares.append(lista[a])
        else:
            impares.append(lista[a])
    par = set(pares)
    impar = set (impares)
    return par,impar


x={23, 45, 76, 84, 91, 52}

print(contar(x))