#Borrador
#Realice un programa que compruebe la mayoria de edad de una persona
#Muestre por pantalla si la persona es mayor o menor de edad

dia = int(input("Ingrese el dia de su nacimiento: "))
mes = int(input("Ingrese el mes de su nacimiento: "))
year = int(input("Ingrese el año de su nacimiento: "))

dia_hoy = int(input("Ingrese el dia de hoy: "))
mes_hoy = int(input("Ingrese el mes de hoy: "))
year_hoy = int(input("Ingrese el año de hoy: "))

edad = year_hoy - year
if (dia_hoy>=dia and mes_hoy>=mes):
    print(f"Usted tiene {edad} años")
else:
    edad = edad - 1
    print(f"Usted tiene {edad} años")

if (edad >= 18):
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

#determine cuantas veces se repiten las vocales en una oracion dada
oracion = "aaaaaaaaaaaaaaaaaaaaaaaeeeeeeeeeeeeeiiiiiiiiiiiiiiiiooou"
cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0

for char in oracion:
    char = char.lower()
    if char == "a":
        cont_a += 1
    elif char == "e":
        cont_e += 1
    elif char == "i":
        cont_i += 1
    elif char == "o":
        cont_o += 1
    elif char == "u":
        cont_u += 1
