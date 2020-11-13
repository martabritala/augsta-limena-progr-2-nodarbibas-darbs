def FtoC (x):
    rez = (x - 32) * 5 / 9
    if rez <= -273.15:
        rez = -273.15
    return rez
