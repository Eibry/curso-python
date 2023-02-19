def wrapper():
    number = int(input("¿Cuál tabla de multiplicar desea conocer? "))

    def nested():
        for i in range(11):
            print(f'{number} x {i} = {number * i}')

    nested()

if __name__ == '__main__':
    wrapper()