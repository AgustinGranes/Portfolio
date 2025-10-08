def mcd(a, b):
  if b == 0:
    return a
  else:
    return mcd(b, a % b)

print(mcd(48, 18))
"Divide el número más grande entre el más pequeño. Quédate con el resto de esa división. Ahora, reemplaza el número más grande por el más pequeño, y el más pequeño por el resto que obtuviste. Repite este proceso hasta que el resto sea 0. El último resto que no fue cero es el MCD de los dos números originales." 