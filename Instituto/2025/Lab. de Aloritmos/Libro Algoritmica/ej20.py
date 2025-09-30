def busqueda_recursiva_centinela(lista, valor, indice):
    if lista[indice] == valor:
        return indice
    return busqueda_recursiva_centinela(lista, valor, indice + 1)

def busqueda_centinela(lista, valor):
    n_original = len(lista)
    lista.append(valor)
    
    indice_encontrado = busqueda_recursiva_centinela(lista, valor, 0)
    
    lista.pop() 
    
    if indice_encontrado < n_original:
        return f"Valor {valor} encontrado en el índice: {indice_encontrado}"
    else:
        return f"Valor {valor} no se encuentra en la lista."

mi_lista = [1, 5, 9, 13, 16, 20, 25]
valor_a_buscar = 16
valor_no_existente = 99

print(busqueda_centinela(mi_lista, valor_a_buscar))
print(busqueda_centinela(mi_lista, valor_no_existente))

# AI