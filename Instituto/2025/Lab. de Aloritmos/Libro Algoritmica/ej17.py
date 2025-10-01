def invertida(lista):
    if lista == []:
        return []
    return [lista[-1]] + invertida(lista[:-1])

print(invertida(['HOLA', 'CHAU', 'MILEI', 'ALGORITMO', 'RECURSIVO']))