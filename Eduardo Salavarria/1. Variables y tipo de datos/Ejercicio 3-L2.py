#Terminado

#Un mensaje se encuentra codificado y para decodificarlo se sabe que cada letra del mensaje son +3 letras en el abecedario ingles (sin incluir la ñ)
#realice un programa que ayude a decodificarlo y encuentre el mensaje escondido en este.

#Utilice slicing
#Nota: Utilice use convenientemente el abecedario que se encuentra ahi

abecedario = "abcdefghijklmopqrstuvwxyzabcdefghijklmopqrstuvwxyz"
mensaje = "ekix"

caracter_1 = mensaje[0]
caracter_2 = mensaje[1]
caracter_3 = mensaje[2]
caracter_4 = mensaje[3]

caracter_abc_1 = abecedario[abecedario.index(caracter_1) + 3]
caracter_abc_2 = abecedario[abecedario.index(caracter_2) + 3]
caracter_abc_3 = abecedario[abecedario.index(caracter_3) + 3]
caracter_abc_4 = abecedario[abecedario.index(caracter_4) + 3]

print(caracter_abc_1+caracter_abc_2+caracter_abc_3+caracter_abc_4)

