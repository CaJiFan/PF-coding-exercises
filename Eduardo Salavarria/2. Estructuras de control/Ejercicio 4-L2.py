
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
    
    