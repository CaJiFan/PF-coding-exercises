import random as rd
lista_1 = ['_']*24
lista_2 = ['_']*24
lista_3 = ['_']*24
player_1 = 'A'
player_2 = 'B'
player_3 = 'C'
print("Iniciando juego")
posiciones = [0,0,0]
jugadores = ['A','B','C']
start = 'ABC'
lista_1[0] = 'A'
lista_2[0] = 'B'
lista_3[0] = 'C'

won = False
jugadas = 0

while (not won):
    for index, jugador in enumerate(jugadores):
        dado = rd.randint(1,6)
        print("Sale numero", dado, "jugador", jugador)
        if jugador == 'A':
            pos_start = posiciones[index]
            posiciones[index] += dado
            pos_final = posiciones[index]
            if (pos_final<len(lista_1)-1):
                lista_1[pos_start] = '_'
                lista_1[pos_final] = 'A'
            else:
                won = True
                lista_1[-1] = 'A'
                lista_1[pos_start] = '_'
                print("Jugador A acaba de ganar")
                
            
        elif jugador == 'B':
            pos_start = posiciones[index]
            posiciones[index] += dado
            pos_final = posiciones[index]
            if (pos_final<len(lista_1)-1):
                lista_2[pos_start] = '_'
                lista_2[pos_final] = 'B'

            else:
                won = True
                lista_2[-1] = 'B'
                lista_2[pos_start] = '_'
                print("Jugador B acaba de ganar")
                
            
        elif jugador == 'C':
            pos_start = posiciones[index]
            posiciones[index] += dado
            pos_final = posiciones[index]
            if (pos_final<len(lista_1)-1):
                lista_3[pos_start] = '_'
                lista_3[pos_final] = 'C'
            else:
                won = True
                lista_3[pos_start] = '_'
                lista_3[-1] = 'C'
                print("Jugador C acaba de ganar")
                

        print(lista_1)
        print(lista_2)
        print(lista_3)