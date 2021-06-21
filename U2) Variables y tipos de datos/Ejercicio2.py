#Realice un programa que pida al usuario que ingrese 2 numeros enteros y muestre en pantalla los resultados de las
# siguientes operaciones:
# SUMA, RESTA, MULTIPLICACION, Y POTENCIACION
#NOTA: suponga que el usuario solo va a ingresar numeros enteros. Tenga en cuenta que el orden del ingreso de los
# numeros afectará el resultado
#Ejemplo:

# INPUT
# Ingrese el primer numero: 4
# Ingrese el segundo numero: 2

# OUTPUT
# SUMA: 6
# RESTA: 2
# MULTIPLICACION: 8
# POTENCIACION: 16

#solucion

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

print("SUMA: ", num1+num2)
print("RESTA: ", num1-num2)
print("MULTIPLICACION: ", num1*num2)
print("POTENCIACION: ", num1**num2)