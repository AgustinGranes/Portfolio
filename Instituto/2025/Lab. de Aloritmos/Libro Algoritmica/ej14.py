def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        return (numero % 10) + suma_digitos(numero // 10)
    
print(suma_digitos(12345))
print(suma_digitos(394))