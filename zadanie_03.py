
miasto_a = input("Miasto A: ")
miasto_b = input("Miasto B: ")
dystans = int(input(f"Dystans {miasto_a}‐{miasto_b}: "))
cena = float(input("Cena paliwa: "))
spalanie = float(input("Spalanie na 100 km: "))

koszt = round((dystans / 100) * spalanie * cena, 2)

print(f"Koszt przejazdu {miasto_a}‐{miasto_b} to {koszt} PLN")