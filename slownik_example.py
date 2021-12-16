SAMOGLOSKI = "aeiouy"
text = "Ala ma kota. Kot ma Ale"

licznik_samoglosek = {}
for znak in text.lower():
    if znak in SAMOGLOSKI:
        licznik_samoglosek[znak] = licznik_samoglosek.get(znak, 0) + 1

print(licznik_samoglosek)