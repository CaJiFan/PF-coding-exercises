#Determine una funcion calcularimc que reciba argumentos de las listas de altura y peso. Retorne una lista con el imc de los jugadores
#Use la formula del imc = peso/altura^2

#Solucion
def calcularimc(altura, peso):
    
    imcJugadores = []
    for i in range(len(altura)):
        alturaM = altura[i]/100 
        imc = peso[i]/(alturaM)**2
        imc = round(imc, 2)
        imcJugadores.append(imc) 
    return imcJugadores
    
#Programe una funcion verificarJugadores que reciba de argumento el nombre de los jugadores y la lista previamente obtenida del IMC
#muestre en pantalla cada uno de los imc de los jugadores.
#Muestre en pantalla los jugadores que tengan un imc menor a 18 e imprima que debe presentarse a consulta medica
#>>> El jugador Eduardo con icm 17.5, debe presentarse a consulta medica.

#Solucion
def verificarJugadores(jugadores, imcJugadores):
    #impresion de los jugadores con imc
    for i in range(len(jugadores)):
        print(f"El jugador {jugadores[i]}, tiene un imc de: {imcJugadores[i]}")

    #impresion de los jugadores con imc < 18
    for i in range(len(jugadores)):
        if imcJugadores[i] < 18:
            print(f"El jugador {jugadores[i]} con imc {imcJugadores[i]}, debe presentarse a consulta medica")

#Determine una funcion maxJugadores que reciba como argumento los jugadores y la lista del IMC que muestre el jugador que tengan IMC mayor de la lista completa de los IMC de
#los jugadores
#>>>El indice de IMC mas alto es/son los jugadores: Juan con un ICM: 30

#Solucion
def maxJugadores(jugadores, np_imc):
    imc_max = max(np_imc)
    jugadores_imcAlto = []
    for i in range(len(jugadores)):
        if np_imc[i] == imc_max:
            jugadores_imcAlto.append(jugadores[i])
    print(f'El indice de IMC mas alto es/son los jugadores: {", ".join(jugadores_imcAlto)} con un ICM: {imc_max}')

#Determine una funcion calcularPromedio que muestre por pantalla el promedio de la lista de IMC de los jugadores.

#Solucion
def calcularPromedio(np_imc):
    promedio = sum(np_imc)/len(np_imc)
    promedio = round(promedio, 2)
    print("El promedio de la lista de IMC es", promedio)