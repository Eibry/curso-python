menu = """Programa para calcular perímetros

Elija una opción:

[1] Cuadrado
[2] Rectángulo
[3] Triángulo
[4] Círculo
[5] Pentágono

Escribe el número de la figura a elegir: """
opcion = int(input(menu))

if opcion == 1:
    print("Calcular el perímetro del cuadrado")
    lado = int(input("¿Cuánto mide uno de sus lados? "))
    respuesta = lado * 4
    print("El perímetro es " + str(respuesta))
elif opcion == 2:
    print("Calcular el perímetro del rectángulo")
    base = int(input("¿Cuánto mide la base? "))
    altura = int(input("¿Cuánto mide la altura? "))
    respuesta = (base * 2) + (altura * 2)
    print("El perímetro es " + str(respuesta))
elif opcion == 3:
    print("Calcular el perímetro del triángulo")
    lado = int(input("¿Cuánto mide uno de sus lados? "))
    respuesta = lado * 3
    print("El perímetro es " + str(respuesta))
elif opcion == 4:
    pi = 3.1426
    print("Calcular el perímetro del círculo")
    diametro = int(input("¿Cuánto mide el diámetro? "))
    respuesta = diametro * pi
    print("El perímetro es " + str(round(respuesta, 2)))
elif opcion == 5:
    print("Calcular el perímetro del pentágono")
    lado = int(input("¿Cuánto mide uno de sus lados? "))
    respuesta = lado * 5
    print("El perímetro es " + str(respuesta))
else:
    print("Elige una opción correcta")