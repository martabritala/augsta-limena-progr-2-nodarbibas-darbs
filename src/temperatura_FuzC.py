def FtoC (x):
    return (x - 32) * 5 / 9
temperature = float(input("Ievadi temperaturu Fahrenheita grados:"))
celsijs =FtoC (temperature)
print("Temperatura Celsija: " , celsijs)