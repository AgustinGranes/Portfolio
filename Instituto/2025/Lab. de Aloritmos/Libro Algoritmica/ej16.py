def obtener_termino_an(n):
    if n == 1:
        return 2
    else:
        return obtener_termino_an(n - 1) * -3

def visualizar_sucesion_hasta_n(n):
    if n < 1:
        return
    visualizar_sucesion_hasta_n(n - 1)
    valor_actual = obtener_termino_an(n)
    print(f"El término a{n} es: {valor_actual}")

visualizar_sucesion_hasta_n(5)

"Totalmente realizado por IA, no entendi el concepto de raiz cuadrada entera y mucho menos su formula matematica."