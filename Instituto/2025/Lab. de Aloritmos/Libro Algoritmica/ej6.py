def invertida(palabra):
    if palabra == "":
        return ""
    return palabra[-1] + invertida(palabra[:-1])

    
print(invertida('HOLA'))
print(invertida('CHAU'))
print(invertida('MILEI'))
print(invertida('ALGORITMO'))
print(invertida('RECURSIVO'))