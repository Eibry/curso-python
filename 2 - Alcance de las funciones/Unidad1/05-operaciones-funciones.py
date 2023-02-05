menu = """Calcular diferentes operaciones aritméticas

Elige una de las siguientes opciones:

[1] Suma
[2] Resta
[3] Multiplicación
[4] División
[5] Residuo o modulo
[6] División entera

Escribe el número de la opción: """

def operacion(mensaje, opcion, operacion):
    print(mensaje + " 2 números")
    numero1 = int(input("Escribe un número "))
    numero2 = int(input("Escribe otro número "))
    if opcion == 1:
        respuesta = numero1 + numero2
    elif opcion == 2:
        respuesta = numero1 - numero2
    elif opcion == 3:
        respuesta = numero1 * numero2
    elif opcion == 4:
        respuesta = numero1 / numero2
    elif opcion == 5:
        respuesta = numero1 % numero2
    elif opcion == 6:
        respuesta = numero1 // numero2
    print(f'{operacion} es: {respuesta}')

opcion = int(input(menu))

if opcion == 1:
    operacion("Sumar", opcion, "La suma")
elif opcion == 2:
    operacion("Restar", opcion, "La resta")
elif opcion == 3:
    operacion("Multiplicar", opcion, "La multiplicación")
elif opcion == 4:
    operacion("Dividir", opcion, "La división")
elif opcion == 5:
    operacion("El residuo de", opcion, "El residuo")
elif opcion == 6:
    operacion("La división entera de", opcion, "La división entera")
else:
    print("Elige una opción correcta")