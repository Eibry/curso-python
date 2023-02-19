def wrapper():
    name = input("Escribe tu nombre ")
    phone = input("Escribe tu numero de teléfono ")
    phone = [i for i in phone if i.isdigit()]
    phone = "".join(phone)
    def nested():
        numero = '(' + phone[0:3] + ')-' + phone[3:6] + '-' + phone[6:]
        print(f'El número de teléfono de {name} es {numero}')
    nested()

if __name__ == '__main__':
    wrapper()