menu = """Calcular el perímetro de las siguientes figuras

[1] Cuadrado
[2] Rectángulo
[3] Triángulo
[4] Círculo
[5] Pentágono

Escribe el número de la opción: """

def perimetros(figura=None, resultado=None):
    if figura is not None:
        print("Elegiste el " + figura)
    if resultado is not None:
        print("El perímetro es: " + str(resultado))

def opciones():
    opcion = int(input(menu))

    if opcion == 1:
        perimetros('cuadrado')
        lado = int(input("¿Cuánto mide su lado? "))
        perimetro = lado * 4
        perimetros(resultado=perimetro)
    elif opcion == 2:
        perimetros('rectángulo')
        base = int(input("¿Cuánto mide su base? "))
        altura = int(input("¿Cuánto mide su altura? "))
        perimetro = (base * 2) + (altura * 2)
        perimetros(resultado=perimetro)
    elif opcion == 3:
        perimetros('triángulo')
        lado = int(input("¿Cuánto mide su lado? "))
        perimetro = lado * 3
        perimetros(resultado=perimetro)
    elif opcion == 4:
        perimetros('círculo')
        diametro = int(input("¿Cuánto mide su diametro? "))
        perimetro = diametro * 3.1416
        perimetros(resultado=perimetro)
    elif opcion == 5:
        perimetros('pentágono')
        lado = int(input("¿Cuánto mide su lado? "))
        perimetro = lado * 5
        perimetros(resultado=perimetro)
    else:
        print("La opción es incorrecta")
        print("Elige de nuevo")
    input()
    opciones()

if __name__ == '__main__':
    opciones()