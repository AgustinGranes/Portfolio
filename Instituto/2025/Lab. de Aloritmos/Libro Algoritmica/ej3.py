def producto(n, m):
    if not isinstance(n, int) or not isinstance(m, int):
        return "Numero no valido"
    if m == 0:
        return 0
    if m == 1:
        return n
    else:
        return n + producto(n, m - 1)

print(producto(8, 6))
print(producto(9, 8))
print(producto(16, 2))