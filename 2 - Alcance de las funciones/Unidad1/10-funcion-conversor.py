menu = """Conversor de monedas

[1] Peso MXN - Dólar USD
[2] Dolar USD - Peso MXN
[3] Peso MXN - Euro EUR
[4] Euro EUR - Peso MXN
[5] Peso MXN - Libra GBP
[6] Libra GBP - Peso MXN

Elige el número de la opción: """

def conversor(moneda_origen, precio, moneda_final):
    cantidad = float(input(f'¿Cuántos {moneda_origen} deseas convertir? '))
    valor = precio * cantidad
    print(f'Son {str(round(valor, 2))} {moneda_final}')

def opciones():
    opcion = int(input(menu))

    if opcion == 1:
        conversor('pesos MXN', 0.054, 'Dolares USD')
    elif opcion == 2:
        conversor('dolares USD', 18.66, 'Pesos MXN')
    elif opcion == 3:
        conversor('pesos MXN', 0.050, 'Euro EUR')
    elif opcion == 4:
        conversor('euro EUR', 19.93, 'Pesos MXN')
    elif opcion == 5:
        conversor('pesos MXN', 0.044, 'Libra GBP')
    elif opcion == 6:
        conversor('libra GBP', 22.51, 'Pesos MXN')
    else:
        print("Ingrese una opción correcta")

if __name__ == '__main__':
    opciones()