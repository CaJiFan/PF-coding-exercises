#Realice un programa donde pida al usuario ingresar una palabra y verifique si la palabra ingresada es palindromo
# (es decir, que al reves sigue siendo la misma palabra). Ademas muestre por consola si es palindromo y como que la
# palabra al reves
#NOTA: el usuario puede ingresar la palabra con mayusculas y minusculas mezcladas, debe limpiar el formato de la
# palabra ingresada (solo mayusculas o minusculas)
#Ejemplo:

# INPUT
# Ingrese una palabra: BaÑo

# OUTPUT
# Es palindromo: False
# Palabra al reves: OÑAB
#############
# INPUT
# Ingrese una palabra: RecoNocer

# OUTPUT
# Es palindromo: True
# Palabra al reves: RECONOCER

#solucion


palabra = input("Ingrese una palabra: ")
palabraLimpia = palabra.upper()
palabraReves = palabraLimpia[::-1]

print("Es palindromo: ", palabraLimpia==palabraReves)
print("Palabra al reves: ", palabraReves)