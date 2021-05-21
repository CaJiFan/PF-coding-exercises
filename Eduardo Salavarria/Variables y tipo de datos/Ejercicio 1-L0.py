#Borrador

#Revise e imprima los tipos de datos que se encuentran en cada variable
#Nota: Diferencie los tipos de datos que puede encontrar en python
#Use la funcion type(var)

var1 = "Hola Mundo"
var2 = 12341
var3 = 3.14
var4 = [1,2,3,4]

print(type(var1))
print(type(var2))
print(type(var3))

#Realice un programa en el que pueda ingresar sus datos personales y muestre por pantalla
#Realice la conversion de datos que sean necesarias para los datos
#por ejemplo si su edad es 18 el tipo de dato debe ser int (entero)

#Nombres
#Apellidos
#Cedula/ID
#Matricula Espol
#Semestre en Curso

#Usar input("descripcion de la accion")

#OUTPUT

#Mis nombres son: Eduardo Emilio
#Mis apellidos son: Salavarria Gomez
#Mi cedula: 0930939143
#Mi matricula: 202017756
#Voy en el semestre: 3

nombre = input("Ingrese su nombre: ")
apellidos = input("Ingrese sus apellidos: ")
cedula = int(input("Ingrese su cedula: "))
edad = int(input("Ingrese su edad: "))
matricula = int(input("Ingrese su matricula ESPOL: "))
semestre = int(input("Ingrese el semestre que esta cursando: "))

print("Mis nombres son", nombre)
print("Mis apellidos son: ", apellidos)
print("Mi cedula:", cedula)
print("Mi edad es:", edad)
print("Voy en el semestre:", semestre)

#Con el uso de python tambien se pueden hacer operaciones matematicas
#como el calculo de areas, perimetros, volumenes de figuras geometricas

#para una esfera de r = 2, r = 3, r = 4, muestre en pantalla:
#   *area
#   *volumen

radio = 2
pi = 3.14

area = 4*pi*((radio)**2)
volumen = 4/3*pi*((radio)**3)
print(area)
print(volumen)