def fibonacci(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)
    
print(fibonacci(1))
print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(16))