saltar = 0
lista = []

while saltar == 0:
    try:
        entrada = input("Agregue un numero (-1, 0 o 1), o presione 9 para saltar: ")
        numero = int(entrada)
        if numero == -1 or numero == 0 or numero == 1:
            saltar = 0
            lista.append(numero)
        elif numero == 9:
            if len(lista) == 0:
                print("Error: Debe ingresar al menos un número antes de saltar")
                print()
            else:
                saltar = 1
                print("Lista sin propagar:", lista)
        else:
            print("Error: El número debe ser -1, 0, 1 o 9")
            print()
    except ValueError:
        print("Error: Debe ingresar un número válido")
        print()

propagar = lista.copy()

for i in range(1, len(propagar)):
    if propagar[i-1] == 0 and propagar[i] == 1:
        propagar[i-1] = 1
    elif propagar[i-1] == 1 and propagar[i] == 0:
        propagar[i] = 1

for i in range(len(propagar)-1, 0, -1):
    if propagar[i-1] == 0 and propagar[i] == 1:
        propagar[i-1] = 1
    elif propagar[i-1] == 1 and propagar[i] == 0:
        propagar[i] = 1

print("Lista Propagada:", propagar)