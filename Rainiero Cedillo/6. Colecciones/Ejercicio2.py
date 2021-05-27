#Escriba un programa que le pida al usuario vegetales con sus cantidades: "vegetal:2",
#estos los irá guardando en una lista de tuplas. Hasta que ingrese -1.
#Muestra al final las tuplas
# NOTA suponga que el usuario ingresara la informacion en el formato que se pide

#Ejemplo
#Ingrese el nombre del vegetal con sus cantidades:vegetal:2
#Ingrese el nombre del vegetal con sus cantidades:Arroz:2
#Ingrese el nombre del vegetal con sus cantidades:Manzana:5
#Ingrese el nombre del vegetal con sus cantidades:-1
#[('vegetal', 2), ('Arroz', 2), ('Manzana', 5)]


#Solucion
tuplas = []
vegetal = input("Ingrese el nombre del vegetal con sus cantidades:")
while vegetal!= "-1":
    nombre,cant = vegetal.split(":")
    tupla= (nombre, int(cant))
    tuplas.append(tupla)
    vegetal = input("Ingrese el nombre del vegetal con sus cantidades:")

print(tuplas)
