def usar_la_fuerza(mochila, indice=0):
    if indice >= len(mochila):
        return (False, 0)
    objeto_actual = mochila[indice]
    if objeto_actual == "sable de luz":
        return (True, 1)
    encontrado_en_el_resto, objetos_sacados_del_resto = usar_la_fuerza(mochila, indice + 1)
    return (encontrado_en_el_resto, 1 + objetos_sacados_del_resto)

mochila_de_luke = ["comida", "mapa estelar", "comunicador", "sable de luz", "botiquín"]
mochila_de_han_solo = ["blaster", "ropa", "herramientas", "dados de la suerte"]
encontrado, objetos_sacados = usar_la_fuerza(mochila_de_luke)