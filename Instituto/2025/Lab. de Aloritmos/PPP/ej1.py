import csv
import sys

def leer_ventas(archivo_ventas):
    try:
        with open(archivo_ventas, mode='r', encoding='utf-8') as archivo:
            lector_csv = csv.reader(archivo)
            next(lector_csv)
            ventas = []
            for fila in lector_csv:
                venta_diccionario = {
                    'titulo': fila[0],
                    'genero': fila[1],
                    'precio': float(fila[2]),
                    'cantidad': int(fila[3])
                }
                ventas.append(venta_diccionario)
            return ventas
        
    except FileNotFoundError:
        print(f"ERROR: El archivo '{archivo_ventas}' no fue encontrado.")
        return []

ventas_leidas = leer_ventas("ventas.csv")
diccionario = ventas_leidas
print(diccionario)

def ingresos_por_genero(ventas):
    ingresos = {}
    for venta in ventas:
        genero = venta['genero']
        ingreso = venta['precio'] * venta['cantidad']
        if genero in ingresos:
            ingresos[genero] += ingreso
        else:
            ingresos[genero] = ingreso
    return ingresos

ingresos = ingresos_por_genero(ventas_leidas)
print(ingresos)

def generar_informe(nombre_archivo):
    ventas = leer_ventas(nombre_archivo)
    if not ventas:
        return
    
    ingresos = ingresos_por_genero(ventas)
    nombre_informe = "informe_ventas.txt"
    
    with open(nombre_informe, 'w', encoding='utf-8') as archivo:
        archivo.write("Ingresos por género:\n\n")
        total = 0
        
        for genero, ingreso in ingresos.items():
            archivo.write(f"{genero}: ${ingreso:.2f}\n")
            total += ingreso
        
        archivo.write(f"\nIngreso total: ${total:.2f}\n")
    
    print(f"Informe creado exitosamente como '{nombre_informe}'")
    return nombre_informe

generar_informe("ventas.csv")