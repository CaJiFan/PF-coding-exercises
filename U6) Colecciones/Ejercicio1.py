#Desarolle la funcion articulos() en python que un texto y calcule el número de
# artículos que posee el texto. Los artículos a contar son: el, la, las, los, un, unos. La
# función recibirá el texto y retornará una lista de tuplas con dos valores


# TEXTO
#"El próximo domingo, los ciudadanos tendrán ocasión de hacer política, de participar en la toma de decisiones públicas,
# cuando depositen su voto para elegir a 194 diputados de mayoría y tal vez cincuenta de partido. La
# electoral les permite, de ese modo ejercer  funciones de gobierno. Pero ¿de verdad es así?. La respuesta tiene
# que ser negativa. La política no se hace en las urnas. El sistema de partido hegemónico que impera en México
# desde 1929 determina que la verdadera elección de diputados haya ocurrido en febrero, probablemente cuando los
# diversos intereses que es aglutinan en el PRI acordaron las candidaturas, en un proceso que sólo es formalmente
# interior, pero que por la naturaleza del partido es el que verdaderamente decide la composición de la Cámara."

#solucion
def articulos(texto):
  texto = texto.lower()
  el = texto.count("el")
  la = texto.count("la")
  las = texto.count("las")
  los = texto.count("los")
  un = texto.count("un")
  unos = texto.count("unos")
  listaTuplas =[("articulo_LA",la),("articulo_EL", el),("articulo_LAS", las),("articulo_LOS", los),("articulo_UN", un),("articulo_UNOS", unos)]
  return listaTuplas

texto = "El próximo domingo, los ciudadanos tendrán ocasión de hacer política, de participar en la toma de decisiones" \
        " públicas, cuando depositen su voto para elegir a 194 diputados de mayoría y tal vez cincuenta de partido." \
        " La democracia electoral les permite, de ese modo ejercer  funciones de gobierno. Pero ¿de verdad es así?." \
        " La respuesta tiene que ser negativa. La política no se hace en las urnas. El sistema de partido hegemónico" \
        " que impera en México desde 1929 determina que la verdadera elección de diputados haya ocurrido en febrero," \
        " probablemente cuando los diversos intereses que es aglutinan en el PRI acordaron las candidaturas, en un " \
        "proceso que sólo es formalmente interior, pero que por la naturaleza del partido es el que verdaderamente" \
        " decide la composición de la Cámara."

print(articulos(texto))