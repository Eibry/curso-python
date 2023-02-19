import os

usuarios = [
    ['Romeo', 'Santana', 33, ['Python']],
    ['María', 'Pérez', 30, ['JavaScript', 'Python', 'C++']],
    ['Juan', 'López', 28, ['HTML', 'CSS', 'JavaScript']],
    ['Laura', 'Rodríguez', 25, ['C++', 'Java']],
    ['Pedro', 'Hernández', 35, ['Java', 'PHP', 'Python']]
]

menu = """Buscar usuarios por:

[N]ombre
[A]pellido
[L]enguaje de programación

Seleccione una opción: """


def buscar(dato):
    users = [user for user in usuarios if user[0] == dato or user[1] == dato]
    tabla(users)

def por_lenguaje(dato):
    users = [user for user in usuarios for i in user[3] if i == dato]
    tabla(users)

def tabla(users):
    print("-" * 60)
    print("| Nombre   | Apellido   | Edad | Lenguajes de programación |")
    print("-" * 60)
    for user in users:
        nombre, apellido, edad, lenguajes = user
        program = ''
        for i in lenguajes:
            program += i + ' '
        print(f'| {nombre}{" " * (8 - len(nombre))} | {apellido}{" " * (10 - len(apellido))} | {edad}{" " * (4 - len(str(edad)))} | {program}{" " * (25 - len(program))} |')
    print("-" * 60)
    input("Presiona una tecla para continuar...")

def index():
    opcion = input(menu).upper()

    if opcion == 'N':
        os.system(clean)
        name = input("Escriba el nombre: ").capitalize()
        buscar(name)
    elif opcion == 'A':
        os.system(clean)
        lastname = input("Escriba el apellido: ").capitalize()
        buscar(lastname)
    elif opcion == 'L':
        os.system(clean)
        lenguaje = input("Escriba el lenguaje: ")
        por_lenguaje(lenguaje)
    else:
        print("Elige una opción correcta!")
        print()
        os.system(clean)
    index()

if __name__ == '__main__':
    if os.name == "posix":
        clean = 'clear'
    elif os.name == "ce" or os.name == "dos" or os.name == "nt":
        clean = 'cls'

    index()
    