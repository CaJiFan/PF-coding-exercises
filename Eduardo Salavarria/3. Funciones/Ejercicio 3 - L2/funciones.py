def calcularimc(altura, peso):
    
    imcJugadores = []
    for i in range(len(altura)):
        alturaM = altura[i]/100 
        imc = peso[i]/(alturaM)**2
        imc = round(imc, 2)
        imcJugadores.append(imc) 
    return imcJugadores

def verificarJugadores(jugadores, imcJugadores):
    #impresion de los jugadores con imc
    for i in range(len(jugadores)):
        print(f"El jugador {jugadores[i]}, tiene un imc de: {imcJugadores[i]}")

    #impresion de los jugadores con imc < 18
    for i in range(len(jugadores)):
        if imcJugadores[i] < 18:
            print(f"El jugador {jugadores[i]} con imc {imcJugadores[i]}, debe presentarse a consulta medica")

def maxJugadores(jugadores, np_imc):
    imc_max = max(np_imc)
    jugadores_imcAlto = []
    for i in range(len(jugadores)):
        if np_imc[i] == imc_max:
            jugadores_imcAlto.append(jugadores[i])
    print(f'El indice de IMC mas alto es/son los jugadores: {", ".join(jugadores_imcAlto)} con un ICM: {imc_max}')

def calcularPromedio(np_imc):
    promedio = sum(np_imc)/len(np_imc)
    promedio = round(promedio, 2)
    print("El promedio de la lista de IMC es", promedio)