def wrapper(number):

    def nested():
        print(number)

    return nested


if __name__ == '__main__':
    my_func = wrapper(5)
    my_func()
    func = wrapper(6)
    func()
    