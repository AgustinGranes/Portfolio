def serie(numero):
    if numero == 1:
        return numero
    else:
        return serie(numero - 1) + 1 / numero
    
print(serie(54))
print(serie(24))
print(serie(6))
print(serie(92))
print(serie(11))   
print(serie(2)) 