import random, time
a = [ ]
b = [ ]

#Generacion de la lista a (SIN ORDENAR)
for i in range(1, 4000000):
    b = random.randint(1, 1000000)
    a.append(b)

b = a.copy()
b.sort()

# Metodo de Busqueda binaria
def busqueda_binaria(a, x):
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = (lo + hi)//2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# Metodo de Busqueda secuencial
def busqueda_secuencial(a, x):
    for i, v in enumerate(a):
        if v == x:
            return i
    return -1

tamaños = [100000, 1000000, 10000000]

for i in tamaños:
    a = [random.randint(1, i) for a in range(i)]
    b = a.copy()
    b.sort()

    inicio = time.time()
    busqueda_binaria(b, 500)
    fin = time.time()
    print('Tiempo con busqueda binaria:', fin- inicio, "segundos")

    inicio2 = time.time()
    busqueda_secuencial(a, 500)
    fin2 = time.time()
    print('Tiempo con busqueda secuencial:', fin2- inicio2, "segundos")