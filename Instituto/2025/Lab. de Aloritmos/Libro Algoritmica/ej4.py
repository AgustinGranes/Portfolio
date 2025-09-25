def potencia(base, exponente):
    if not isinstance(base, int) or not isinstance(exponente, int):
        return "Numero no valido"
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

print(potencia(8, 6))
print(potencia(9, 8))
print(potencia(16, 2))