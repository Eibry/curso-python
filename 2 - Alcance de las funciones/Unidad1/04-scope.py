nombre = 'Romeo'

def saludo():
    global nombre
    nombre = 'Pedro'
    print("Hola")
    print("Mucho gusto " + nombre)
    
print(nombre)
saludo()
print(nombre)