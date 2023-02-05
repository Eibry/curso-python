numero = int(input("Escribe un número entero: "))

def fibonacci(numero):
    if numero == 1:
        return 1
    elif numero == 0:
        return 0

    return fibonacci(numero - 1) + fibonacci(numero - 2)

for i in range(numero):
    print(fibonacci(i))