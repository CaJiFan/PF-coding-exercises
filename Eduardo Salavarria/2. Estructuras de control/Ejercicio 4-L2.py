#Terminado

#En el juego que usted tiene que crear tiene una lista a su disposicion con la vida en total de los patos que tiene que matar
#cada pato esta representado como un elemento de la lista
# EJEMPLO:
#   lista_vida = [5,5,5,5,5]
#pida al usuario ingresar una posicion en la que quiere disparar a la lista
#Realice un programa en que ayude a matar los patos con 25 tiros
#Si se terminan los tiros y ha matado todos los patos usted gana
#Si se terminan los tiros y NO ha matado a todos los patos usted pierde

#Recuerde que cada vez que falla o le da a un pato se pierde un tiro

#Solucion
lista_vida = [1,0,0,0,1]
tiros = 10
while sum(lista_vida) > 0:
    print("Todavia le puede seguir quitando vida")
    print(lista_vida)
    pos_usuario = int(input("Ingrese a que pato le quiere dar: "))
    indice = pos_usuario - 1
    vida_indice = lista_vida[indice]
    if vida_indice > 0:
        lista_vida[indice] = lista_vida[indice] - 1
        lista_vida = lista_vida
        tiros -= 1
        print("Le acaba de dar a un pato")
        print("-1 TIRO")
    else:
        print("Acaba de perder un tiro")
        print("-1 TIRO")
        tiros -= 1
    
print("Usted mato a todos los patos")
    
    