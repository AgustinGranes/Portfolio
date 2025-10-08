def romanos(numero):
    valores = {
        'I':1, 
        'V':5, 
        'X':10, 
        'L':50, 
        'C':100, 
        'D':500, 
        'M':1000,
    }
    if not numero:
        return 0
    if len(numero) == 1:
        return valores[numero]
    
    primero = valores[numero[0]]
    segundo = valores[numero[1]]

    if primero < segundo:
        return segundo - primero + romanos(numero[2:])
    else:
        return primero + romanos(numero[1:])
    
print(romanos('III'))
print(romanos('LXXXIX'))
print(romanos('CCXXXVII'))
print(romanos('MCMXLVII'))
print(romanos('DXLII'))