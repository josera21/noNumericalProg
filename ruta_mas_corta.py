def ruta_mas_corta(ciudades, deposito):
  distancias = []
  indices_usados = []

  for i in range(0, len(ciudades)):
    distancias.append(ciudades[deposito][i])
  km_acumulado = min(distancias)
  index_sig = ciudades[deposito].index(min(distancias)) # Retorna el indice donde se encuentra el minimo
  indices_usados.append(deposito)
  indices_usados.append(index_sig)

  print "Deposito en C{}".format(deposito + 1)
  print "Minimo: {}".format(km_acumulado)

  for i in range(1, len(ciudades)):
    print "Siguiente ciudad C{}".format(index_sig + 1)
    act_ciudad = ciudades[index_sig]
    # Recorriendo ciudad actual.
    for k in range(1, len(act_ciudad) + 1):
      if ((k - 1) == deposito):
        continue
      else:
        dist = act_ciudad[k - 1]
        if ((dist + km_acumulado) < distancias[k - 1]):
          distancias[k - 1] = dist + km_acumulado
    # Buscando los minimos entre los resultados
    minimo = 99999999
    for j in range(0, len(distancias)):
      if j == deposito:
        continue
      if ((minimo > distancias[j]) and (j not in indices_usados)):
        minimo = distancias[j]
        km_acumulado = minimo
    if minimo == 99999999:
      break
    else:
      print "minimo {}".format(minimo)
      index_sig = distancias.index(minimo) # Retorna el indice donde se encuentra el minimo
      indices_usados.append(index_sig)

  return distancias
  

if __name__ == "__main__":
  # Ruta mas corta desde vertice unico

  matrix = [
    [99999, 90, 58, 85, 99999, 99999],
    [80, 99999, 99999, 55, 99999, 99999],
    [50, 99999, 99999, 61, 99999, 15],
    [85, 45, 70, 99999, 99999, 130],
    [99999, 99999, 99999, 99999, 99999, 45],
    [99999, 99999, 20, 150, 45, 99999]
  ]

  san_felipe = ruta_mas_corta(matrix, 0)
  print "*** San Felipe ***"
  for i in range(0, len(san_felipe)):
    print "Distancia a C{} es: {}".format((i + 1), san_felipe[i])
  print "*"*10
  barquisimeto = ruta_mas_corta(matrix, 3)
  print "*** Barquisimeto ***"
  for i in range(0, len(barquisimeto)):
    print "Distancia a C{} es: {}".format((i + 1), barquisimeto[i])
  print "*"*10
  tocuyo = ruta_mas_corta(matrix, 4)
  print "*** tocuyo ***"
  for i in range(0, len(tocuyo)):
    print "Distancia a C{} es: {}".format((i + 1), tocuyo[i])