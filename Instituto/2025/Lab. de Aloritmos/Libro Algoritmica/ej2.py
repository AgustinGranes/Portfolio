def suma(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return numero * (numero + 1) / 2

print(suma(8))
print(suma(9))
print(suma(16))