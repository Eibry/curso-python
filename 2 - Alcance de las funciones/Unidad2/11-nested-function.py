def wrapper():
    name = input("Escribe tu nombre ")
    lastname = input("Escribe tu apellido ")
    
    def nested():
        print(f'Mucho gusto {name} {lastname}')
    
    nested()

wrapper()