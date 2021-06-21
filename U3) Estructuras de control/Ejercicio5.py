#Realice un programa que pida al usuario que ingrese un numero y ese numero sera el numero de niveles de una piramide
# del signo #. Si el numero ingresado es menor o igual a 0 mostrar mensaje de error y terminar el programa.

#NOTA: utilice for dentro de for como consejo, y los print con end. Suponer que el usuario no ingresara letras

# EJEMPLO:
#Ingrese el número de niveles de la pirámide: 7
      #
     ###
    #####
   #######
  #########
 ###########
#############



#solucion
n = int(input("Ingrese el número de niveles de la pirámide: "))
if (n>=1):
  fila = 0
  for i in range(1,n+1):
    fila +=2
    for j in range(n-i):
      print (" ",end="")
    for k in range(i,fila):
      print ("#",end="")
    for l in range(fila-2,i-1,-1):
      print ("#",end="")        
    print ()
else:
  print("Error")