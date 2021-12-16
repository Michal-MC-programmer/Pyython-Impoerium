dane = []

for i in range(10):
    operacja = input("Podaj liczbe lub k by zakonczyc: ")
    if operacja == "k":
        break
    liczba = int(operacja)
    dane.append(liczba)
    
print(sum(dane) / len(dane))
