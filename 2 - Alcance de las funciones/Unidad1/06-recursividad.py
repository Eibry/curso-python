def saludo():
    nombre = input("¿Cómo te llamas? ")
    print("Mucho gusto " + nombre)
    if nombre == '':
        return
    saludo()

saludo()