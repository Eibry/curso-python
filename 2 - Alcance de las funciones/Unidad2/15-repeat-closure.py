def wrapper(number):
    def nested(string):
        print(f'{string * number}')
    return nested

if __name__ == '__main__':
    repeat_4 = wrapper(4)
    repeat_4('hola ')
    repeat_6 = wrapper(6)
    repeat_6('adiós ')