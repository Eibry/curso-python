USER = 'username'
PASSWORD = 'qwerty'

def login():
    user = input("Escribe tu usuario: ")
    password = input("Escribe tu contraseña: ")
    
    def correct():
        print("Acceso autorizado")
    
    def incorrect():
        print("Acceso denegado")
        if user != USER and password == PASSWORD:
            print("Usuario incorrecto")
        elif password != PASSWORD and user == USER:
            print("Contraseña incorrecta")
        else:
            print("Datos incorrectos")
    
    def verif():
        if user == USER and password == PASSWORD:
            correct()
        else:
            incorrect()
            login()
    
    verif()

if __name__ == '__main__':
    login()


