def _raiz_recursiva(n, i):
    if i * i > n:
        return i - 1
    else:
        return _raiz_recursiva(n, i + 1)

def raiz_cuadrada_entera(n):
    if n < 0:
        raise ValueError("El número no puede ser negativo")
    return _raiz_recursiva(n, 0)

"Totalmente realizado por IA, no entendi el concepto de raiz cuadrada entera y mucho menos su formula matematica."