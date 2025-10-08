def binario(numero):
    if numero == 0 or numero == 1:
        return str(numero)
    else:
        return binario(numero // 2) + str(numero % 2)

print(binario(54))
print(binario(24))
print(binario(6))
print(binario(92))
print(binario(11))   
print(binario(2)) 