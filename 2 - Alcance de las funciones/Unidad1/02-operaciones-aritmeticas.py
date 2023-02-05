menu = """Calcular diferentes operaciones aritméticas

Elige una de las siguientes opciones:

[1] Suma
[2] Resta
[3] Multiplicación
[4] División
[5] Residuo o modulo
[6] División entera

Escribe el número de la opción: """

opcion = int(input(menu))

if opcion == 1:
    print("Sumar 2 números")
    numero1 = int(input("Escribe un número "))
    numero2 = int(input("Escribe otro número "))
    respuesta = numero1 + numero2
    print("La suma es: " + str(respuesta))
elif opcion == 2:
    print("Restar 2 números")
    numero1 = int(input("Escribe un número "))
    numero2 = int(input("Escribe otro número "))
    respuesta = numero1 - numero2
    print("La resta es: " + str(respuesta))
elif opcion == 3:
    print("Multiplicar 2 números")
    numero1 = int(input("Escribe un número "))
    numero2 = int(input("Escribe otro número "))
    respuesta = numero1 * numero2
    print("La multiplicación es: " + str(respuesta))
elif opcion == 4:
    print("Dividir 2 números")
    numero1 = int(input("Escribe un número "))
    numero2 = int(input("Escribe otro número "))
    respuesta = numero1 / numero2
    print("La división es: " + str(respuesta))
elif opcion == 5:
    print("El residuo de 2 números")
    numero1 = int(input("Escribe un número "))
    numero2 = int(input("Escribe otro número "))
    respuesta = numero1 % numero2
    print("El residuo es: " + str(respuesta))
elif opcion == 6:
    print("La división entera de 2 números")
    numero1 = int(input("Escribe un número "))
    numero2 = int(input("Escribe otro número "))
    respuesta = numero1 // numero2
    print("La división entera es: " + str(respuesta))
else:
    print("Elige una opción correcta")