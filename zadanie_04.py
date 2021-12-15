import datetime

cur_date = datetime.datetime.now()
current_year = cur_date.year

b_year = int(input("Podaj rok urodzenia: "))

if current_year - b_year >= 18:
    print("Jesteś pełnoletni")
else:
    print("Nie jesteś pełnoletni!")