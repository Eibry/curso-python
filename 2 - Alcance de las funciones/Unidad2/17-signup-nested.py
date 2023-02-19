import os

menu = """Control de usuarios

[1] Registrar nuevo usuario
[2] Iniciar sesión

Escribe el número de la opción: """
accounts = []

def signup():
    account = []
    print("Escribe los siguientes datos")
    username = input("Usuario: ")
    email = input("Correo electrónico: ")

    def contraseña():
        password = input("Contraseña: ")
        conf_password = input("Confirmar contraseña: ")
        if password == conf_password:
            return password
        else:
            os.system(clean)
            print("La contraseña no coincide")
            contraseña()

    password = contraseña()


    account = [username, email, password]
    accounts.append(account)
    os.system(clean)
    index()

def login():
    user = input("Escribe tu usuario: ")
    password = input("Escribe tu contraseña: ")

    def correct():
        print("Acceso autorizado")

    def incorrect():
        print("Acceso denegado")

    def verify():
        usuario = None
        # account = [i for i in accounts if account[0] == user or account[1] == user]
        for account in accounts:
            if account[0] == user or account[1] == user:
                usuario = account

        if usuario is not None:
            if password == usuario[2]:
                correct()
                index()
            else:
                incorrect()
                login()
        else:
            os.system(clean)
            print("El usuario no está registrado")
            yesno = input("¿Desea registrarlo? (y/n)")
            if yesno == 'y' or yesno == 'Y':
                os.system(clean)
                signup()
            else:
                os.system(clean)
                index()


    verify()

def index():
    opcion = int(input(menu))
    if opcion == 1:
        os.system(clean)
        signup()
    elif opcion == 2:
        os.system(clean)
        login()
    else:
        print("Opción incorrecta ❌")
    os.system(clean)

if __name__ == '__main__':
    if os.name == "posix":
        clean = 'clear'
    elif os.name == "ce" or os.name == "dos" or os.name == "nt":
        clean = 'cls'
    index()