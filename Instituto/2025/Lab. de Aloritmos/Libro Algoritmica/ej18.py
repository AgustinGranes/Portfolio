def normal(lista):
    if lista == []:
        return []
    return [lista[0]] + normal(lista[1:])

print(normal(['HOLA', 'CHAU', 'MILEI', 'ALGORITMO', 'RECURSIVO']))