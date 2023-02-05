minutes = 5
while minutes >= 0:
    seconds = 59
    while seconds >= 0:
        if seconds < 10:
            print(f'0{minutes}:0{seconds}')
        else:
            print(f'0{minutes}:{seconds}')
        seconds -= 1
    minutes -= 1