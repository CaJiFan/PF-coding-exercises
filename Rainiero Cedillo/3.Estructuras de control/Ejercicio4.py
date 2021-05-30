#Realice un programa que pida nombres de animales, y que indique a que tipo de animal pertenece (mamiferos, aves, etc).
# Debe mostrar un menu de los tipos de animales para que ingresen escribiendo una sola letra. en caso de que escriba mal,
# mostrar por pantalla que el animal no se añadio a la lista
#El programa se acaba cuando el usuario ingresa como nombre el numero 0. 
#El programa guarda el nombre de los animales en 5 diferentes listas y las muestra solo cuando se termine el programa.

#NOTA: sin importar como escriba el nombre el usuario usted debe guardarlo en mayusculas.

#Ejemplo:

#Ingrese el nombre de un animal: leon
#Mamifero: M
#Ave: A
#Reptil: R
#Anfibio: AN
#Pez: P
#Ingrese que tipo es: m

#Ingrese el nombre de un animal: 0

#....

#Mamiferos:  ['LEON']
#Aves:  ['PALOMA']
#Reptiles:  ['COCODRILO']
#Peces:  ['ATUN']
#Anfibios:  ['RANA']



#solucion

mamiferos= []
anfibios= []
aves= []
peces= []
reptiles= []
animal = ""
print("Bienvenido")
while animal!= "0":
  animal = input("Ingrese el nombre de un animal: ").upper()
  if animal!="0":
    print("Mamifero: M")
    print("Ave: A")
    print("Reptil: R")
    print("Anfibio: AN")
    print("Pez: P")
    tipo = input("Ingrese que tipo es: ").upper()
    if tipo=="M":
      mamiferos.append(animal)
    elif tipo=="A":
      aves.append(animal)
    elif tipo=="AN":
      anfibios.append(animal)
    elif tipo=="P":
      peces.append(animal)
    elif tipo=="R":
      reptiles.append(animal)
    else:
      print("El animal no fue agregado")
  print()
print("Mamiferos: ", mamiferos)
print("Aves: ", aves)
print("Reptiles: ", reptiles)
print("Peces: ", peces)
print("Anfibios: ", anfibios)