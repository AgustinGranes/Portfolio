import random, time
a = [ ]

# Generacion de la lista a
for i in range(1, 4000000):
    b = random.randint(1, 10000000)
    a.append(b)

# Primer Metodo: QUICK SORT
def quicksort(a, low=0, high=None):
    if high is None:
        high = len(a)-1
    if low < high:
        p = partition(a, low, high)
        quicksort(a, low, p)
        quicksort(a, p+1, high)
    return a

def partition(a, low, high):
    pivot = a[(low+high)//2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while a[i] < pivot:
            i += 1
        j -= 1
        while a[j] > pivot:
            j -= 1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]

# Segundo Metodo: Heap Sort
def sift_down(a, start, n):
    root = start
    while True:
        child = 2*root + 1
        if child >= n:
            break
        if child+1 < n and a[child] < a[child+1]:
            child += 1
        if a[root] < a[child]:
            a[root], a[child] = a[child], a[root]
            root = child
        else:
            break

def heapify(a):
    n = len(a)
    for i in range(n//2 - 1, -1, -1):
        sift_down(a, i, n)

def heap_sort(a):
    n = len(a)
    heapify(a)
    for end in range(n-1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(a, 0, end)
    return a

# Tercer Metodo: Counting Sort
def counting_sort(a, k=None):
    if not a:
        return []
    if k is None:
        k = max(a)
        count = [0] * (k+1)
    for v in a:
        count[v] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]
    out = [0] * len(a)
    for v in reversed(a):
        out[count[v]-1] = v
        count[v] -= 1
    return out

inicio = time.time()
quicksort(a)
fin = time.time()
print('Tiempo con Quick Sort: ', fin- inicio, "segundos")

inicio2 = time.time()
heap_sort(a)
fin2 = time.time()
print('Tiempo con Heap Sort: ', fin2- inicio2, "segundos")

inicio3 = time.time()
counting_sort(a)
fin3 = time.time()
print('Tiempo con Counting Sort: ', fin3- inicio3, "segundos")