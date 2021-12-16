minimum = None
maksimum = None

while True:
    polecenie = input("Podaj liczbę lub wpisz 'k' by zakończyć: ")
    if polecenie == "k": break

    # if polecenie.isnumeric():
    #     liczba = int(polecenie)
    # else:
    #     print("Podaj liczbę!!")
    #     continue

    try:
        liczba = int(polecenie)
    except ValueError:
        print("Podaj liczbę!!")
        continue

    if minimum is None:
        minimum = liczba
        maksimum = liczba
    else:
        if liczba < minimum:
            minimum = liczba
        if liczba > maksimum:
            maksimum = liczba

print(f"Min: {minimum}, Max: {maksimum}")