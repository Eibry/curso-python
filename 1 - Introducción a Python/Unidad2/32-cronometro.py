minutes = 0
while minutes < 3:
    seconds = 0
    while seconds < 60:
        if seconds < 10:
            print(f'0{minutes}:0{seconds}')
        else:
            print(f'0{minutes}:{seconds}')
        seconds += 1
    minutes += 1