## Funkcje

### *args, **kwargs

#### Zadanie

Zaimplementuj funkcję formatującą podane napisy.

Przykład użycia:

    >>> formatuj(
            'koszt $cena PLN',
            'kwota $cena brutto',
    cena=10, )
    'koszt 10 PLN\nkwota 10 brutto'

### Rekurencja

#### Zadanie

Zaimplementuj funkcję obliczającą silnie dla zadanej wartości. Przykład użycia:

    >>> silnia(5)
    120

#### Zadanie

Zaimplementuj funkcję spłaszczającą podaną listę. Przykład użycia:

    >>> splaszcz([1, 2, 3, [4, 5, [6]], 7])
    [1, 2, 3, 4, 5, 6, 7]

### Lambda.

### Funkcja jako argument

Zaimplementuj funkcję przycinającą listę na podstawie podanego warunku początkowego oraz końcowego:
Przykład użycia:

    >>> przytnij(
            data=[1, 2, 3, 4, 5, 6, 7],
    start=lambda x: x > 3,
    stop=lambda x: x == 6, )
    [4, 5, 6]

### Zasięgi zmiennych

### Domknięcie

### Dekorator

#### Zadanie

Zaimplementuj zestaw dekoratorów otaczających zwracany przez funkcję napis tagami HTML (pogrubienie, podkreślenie,
przekreślenie):
Przykład użycia:

    @bold
    @italic
    def foo(arg):
        return f'To jest {arg}' 

#### Zadanie

Zaimplementuj dekorator wypisujący wywołanie danej funkcji (nazwa i argumenty) oraz czas jej wykonania. Przykład użycia:

    @log
    def foo(arg):
        return f'To jest {arg}'

## Klasy

### Atrybut klasowy

### Atrybut instancji (metoda __init__)

#### Zadanie

Zaimplementuj klasę Product przechowującą informację o cenie, nazwie oraz ID produktu. Zaimplementuj metodę wypisującą
informację o produkcie na konsolę. Przykład użycia:

    >>> product = Product(1, 'Woda', 10.99)
    >>> product.print_info()
    Produkt "Woda", id: 1, cena: 10.99 PLN

#### Zadanie

Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu pracy oraz wypłacanie pensji na podstawie zadanej stawki
godzinowej. Jeżeli pracownik będzie pracował więcej niż 8 godzin (podczas pojedynczej rejestracji czasu) to kolejne
godziny policz jako nadgodziny (z podwójną stawką godzinową). Przykład użycia:

    >>> employee = Employee('Jan', 'Nowak', 100.0)
    >>> employee.register_time(5)
    >>> employee.pay_salary()
    500.0
    >>> employee.pay_salary()
    0.0
    >>> employee.register_time(10)
    >>> employee.pay_salary()
    1200.0

### Atrubuty prywatne

#### Zadanie

Zaimplementuj klasę CashMachine umożliwiającą wpłacanie i wypłacanie pieniędzy. Zadbaj o to aby stan bankomatu
przetrzymywany był w zmiennych prywatnych. Przykład użycia:

    >>> cash_machine = CashMachine()
    >>> cash_machine.is_available
    False
    >>> cash_machine.put_money([200, 100, 100, 50])
    >>> cash_machine.is_available
    True
    >>> cash_machine.withdraw_money(150)
    [100, 50]

#### Zadanie

Zaimplementuj klasę ElectricCar odwzorowującą zachowanie samochodu elektrycznego. Klasa powinna umożliwiać pokonanie
zadanego dystansu, który nie może przekroczyć maksymalnego zasięgu zdefiniowanego dla samochodu. Samochód powinien mieć
także możliwość naładowania baterii.

    >>> car = ElectricCar(100)
    >>> car.drive(70)
    70
    >>> car.drive(50)
    30
    >>> car.drive(50)
    0
    >>> car.charge()
    >>> car.drive(50)
    50

### Atrybuty dynamiczne (+setter)

#### Zadanie

Zaimplementuj klasę Circle

    >>> circle = Circle(1)
    >>> circle.diameter 
    2
    >>> circle.circumference
    6.283185307179586
    >>> circle.diameter = 4
    >>> circle.circumference    
    25.132741228718345
    >>> circle.area
    50.26548245743669

### Przeciążanie operatorów

#### Zadanie

Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora swobodnego na dwuwymiarowej płaszczyźnie. Wektory
powinny mieć możliwość dodawania, odejmowania, mnożenia (przez inny wektor i przez liczbę), porównywania (po długości)
oraz powinny posiadać czytelną reprezentację napisową. Przykład użycia:

    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1 + vector_2

## Argumenty skryptu - sys.argv

## Praca z plikami

#### Zadanie

Napisz program wypisujący na konsolę zawartość wskazanego pliku wraz z numerami linii. Obsłuż sytuację, gdy użytkownik
nie poda nazwy pliku lub poda błędną nazwę. Przykład użycia:

    $ python test.txt
    1: pierwsza linia pliku
    2: druga linia pliku

#### Zadanie

Napisz program wczytujący plik z logami aktywności użytkowników w systemie. Na podstawie wczytanych danych wyświetl
informację o sumarycznym czasie przebywania każdego użytkownika w systemie. Przykład użycia:

    $ python read_logs.py logs.txt
    Czas przebywania w systemie:
    - user-1: 92 s
    - user-2: 51 s
    - user-3: 20 s

## Moduły i paczki

#### Zadanie

Utwórz następującą strukturę pakietów i modułów:

* główny pakiet mathematica
* pakiet wewnętrzny geometry
* moduł figures w pakiecie geometry z funkcjami square_area oraz triangle_area
* pakiet wewnętrzny algebra
* moduł matrices w pakiecie algebra z funkcją add_matrices i sub_matrices
* główny pakiet tests
* moduł test_geometry testujący funkcje geometryczne
* moduł test_algebra testujący funkcje algebraiczne

## JSON

#### Zadanie

Napisz program obsługujący bazę danych pracowników. W bazie danych przechowuj imię, nazwisko, email, rok urodzenia,
pensję. Skorzystaj z modułu json. Przykład użycia:

    $ python employees.py
    Co chcesz zrobić? [d - dodaj, w - wypisz] d
    Imie: Jan
    Nazwisko: Nowak
    Rok urodzenia: 1980
    Pensja: 5000.0
    $ python employees.py
    Co chcesz zrobić? [d - dodaj, w - wypisz] w
    Pracownicy:
    - [1] Jan Nowak - rok: 1980, pensja: 5000.00 PLN

## Tkinter

```python
    import tkinter
from tkinter import messagebox


def policz_sume():
    try:
        a = int(a_entry.get())
        b = int(b_entry.get())
        wynik_label.configure(text=f'Wynik: {a + b}')
    except ValueError:
        messagebox.showerror('Błędne dane!', 'Musisz wprowadzić wartości liczbowe!')


root = tkinter.Tk()
root.columnconfigure(1, weight=1)
a_label = tkinter.Label(master=root, text='a')
a_label.grid(row=0, column=0)
a_entry = tkinter.Entry(master=root)
a_entry.grid(row=0, column=1, sticky=tkinter.EW)
b_label = tkinter.Label(master=root, text='b')
b_label.grid(row=1, column=0)
b_entry = tkinter.Entry(master=root)
b_entry.grid(row=1, column=1, sticky=tkinter.EW)
policz_button = tkinter.Button(master=root, text='Policz', command=policz_sume)
policz_button.grid(row=3, column=0)
wynik_label = tkinter.Label(master=root, text='Wynik: - ')
wynik_label.grid(row=3, column=1, sticky=tkinter.EW)
root.title('Sumator')
root.mainloop()
```

#### Zadanie

Napisz program z graficznym interfejsem użytkownika (GUI) do obliczania kosztów przejazdu na zadanym dystansie na
podstawie spalania samochodu oraz ceny paliwa. Skorzystaj z modułu tkinter.

## Requests

#### Zadania

Napisz program wyświetlający pogodę dla wskazanej przez użytkownika lokalizacji. Skorzystaj z modułu urllib.request,
json oraz API MetaWeather.

## Re

Napisz program znajdujący w dostarczonym pliku wszystkie wystąpienia:

* kodów pocztowych - 12-123
* adresów email - test@email.com
* dat - 12 Jan 1990 Skorzystaj z modułu re.
