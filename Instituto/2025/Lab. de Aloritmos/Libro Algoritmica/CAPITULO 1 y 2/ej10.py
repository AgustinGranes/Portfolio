def contar_digitos(n):
  n = abs(n)
  if n < 10:
    return 1
  else:
    return 1 + contar_digitos(n // 10)