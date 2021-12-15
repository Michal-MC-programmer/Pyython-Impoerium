dni = 7
pytan = 0
temp = 0

while pytan < dni:
    temp += int(input(f"Podaj temperaturę w dniu {pytan + 1}: "))
    pytan += 1

srednia = temp / 7

print("Średnia temperatura:", srednia)