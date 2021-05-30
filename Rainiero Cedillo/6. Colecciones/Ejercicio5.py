#Desarrolle función edadesDivorcio() la función recibe una lista de datos y retorna un diccionario con las
# siguientes características:
#{ 'Azuay': [ (33 , 38), (15, 23)...], 'Pichincha': [ (20 , 38), (20, 53) ...]

#Tip: la provincia está en la columna 1, la edad del hombre está en la columna 25 y la de la mujer en la columna 40

#Usar la Siguiente lista
lista =[['1', 'Azuay', 'Cuenca', 'San Blas', '2016', 'Octubre', '26', '10/26/2016', '2010', 'Abril', '6', '4/6/2010',
  '2001', 'Abril', '27', '4/27/2001', 'No', '15', '10', 'Extranjero', 'US', '1979', '7', '25', '7/25/1979', '37',
  '0', 'Mestizo', 'Si', 'Secundaria', 'Exterior', 'Exterior', 'Exterior', 'Urbana', 'Ecuatoriana', 'EC', '1978',
  '4', '5', '4/5/1978', '38', '0', 'Mestiza', 'Si', 'Secundaria', 'Azuay', 'Cuenca', 'Monay', 'Urbana'],
 ['1', 'Pichincha', 'Quito', 'Quitumbe', '2016', 'Octubre', '10', '10/10/2016', '2016', 'Septiembre', '30',
  '9/30/2016', '2016', 'Marzo', '7', '3/7/2016', 'Se ignora', '1', '1', 'Ecuatoriano', 'EC', '1977', '2', '26',
  '2/26/1977', '39', '0', 'Mestizo', 'Si', 'Secundaria', 'Pichincha', 'Quito', 'Quito Distrito Metropolitano',
  ' cabecera cantonal', ' capital provincial', 'Urbana', 'Ecuatoriana', 'EC', '1966', '10', '20', '10/20/1966',
  '49', '0', 'Mestiza', 'Si', 'Secundaria', 'Bol�var', 'Las Naves', 'Las Mercedes', 'Urbana'],
 ['1', 'Bolivar', 'Guaranda', '�ngel Polibio Ch�ves', '2016', 'Febrero', '10', '2/10/2016', '2016',
  'Enero', '28', '1/28/2016', '1983', 'Octubre', '5', '10/5/1983', 'No', '32', '10', 'Ecuatoriano',
  'EC', '1965', '3', '31', '3/31/1965', '50', '0', 'Mestizo', 'Si', 'Superior', 'Bol�var', 'Las Naves',
  'Las Naves', ' cabecera cantonal', 'Urbana', 'Ecuatoriana', 'EC', '1966', '9', '15', '19','9/15/1966', '49',
  '0', 'Mestiza', 'Si', 'Superior', 'Bol�var', 'Las Naves', 'Las Naves', ' cabecera cantonal', 'Urbana'],
 ['1', 'Pichincha', 'Quito', 'Quitumbe', '2016', 'Diciembre', '20', '12/20/2016', '2016', 'Noviembre', '23',
  '11/23/2016', '2014', 'Diciembre', '15', '12/15/2014', 'No', '2', '1', 'Extranjero', 'US', '1951', '3', '28',
  '3/28/1951', '65', '0', 'Blanco', 'Si', 'Se ignora', 'Exterior', 'Exterior', 'Exterior', 'Urbana', 'Ecuatoriana',
  'EC', '1969', '3', '1', '3/1/1969', '47', '0', 'Mestiza', 'Si', 'Se ignora', 'Exterior', 'Exterior', 'Exterior', 'Urbana']]
#OUTPUT:
#{'Azuay': [(37, 38)], 'Pichincha': [(39, 20), (65, 47)], 'Bolivar': [(50, 19)]}


#Solucion
def edadesDivorcio(lista):
    prov = []
    edadH = []
    edadM= []
    for datos in lista:
        prov.append(datos[1])
        edadH.append(datos[25])
        edadM.append(datos[40])
    prov2 = []
    edades = []
    for a in range(len(prov)):
        tupla = (int(edadH[a]), int(edadM[a]))
        if prov[a] not in prov2:
            prov2.append(prov[a])
            edades.append([tupla])
        else:
            indice = prov2.index(prov[a])
            edades[indice].append(tupla)
    dicc= dict(zip(prov2, edades))
    return dicc

print(edadesDivorcio(lista))