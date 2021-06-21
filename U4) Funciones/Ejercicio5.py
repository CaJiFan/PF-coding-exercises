#Realiza una función decimal(n) que recibe un numero binario y devuelve como resultado un int, que es la conversion en
# decimal del binario ingresar.
#NOTA: la funcion decimal recibe un string con el numero binario


# decimal("10110")
# Output:
# 22


#solucion
def decimal(n):
  n = list(n)
  n.reverse()
  numero = 0
  for a in range(len(n)):
      numero += int(n[a]) * 2 ** a
  return numero

print(decimal("10110"))