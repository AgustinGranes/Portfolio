def busqueda_binaria_recursiva(lista, valor, inicio, fin):
    if inicio > fin:
        return False
        
    medio = (inicio + fin) // 2
    
    if lista[medio] == valor:
        return True
    elif valor < lista[medio]:
        return busqueda_binaria_recursiva(lista, valor, inicio, medio - 1)
    else:
        return busqueda_binaria_recursiva(lista, valor, medio + 1, fin)

def busqueda_binaria(lista, valor):
    resultado = busqueda_binaria_recursiva(lista, valor, 0, len(lista) - 1)
    return f"¿Se encontró el valor {valor}?: {resultado}"

mi_lista_ordenada = [4, 10, 23, 31, 45, 51, 67, 88, 99, 101]
valor_a_buscar = 67
valor_no_existente = 50

print(busqueda_binaria(mi_lista_ordenada, valor_a_buscar))
print(busqueda_binaria(mi_lista_ordenada, valor_no_existente))

# IA