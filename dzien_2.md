# Dzień 2

## Podstawowe struktury danych

### Tupla

#### Zadanie

W sesji interaktywnego środowiska interpretera stwórz tuplę zawierającą 10 różnych liczb całkowitych. Korzystając z operatora dostępu oraz wycinania pobierz:
- drugi element
- przedostatni element
- elementy od trzeciego do siódmego (włącznie) 􏰀 co trzeci element
- co drugi element licząc od końca

### Lista

### Range

#### Zadanie

Napisz program obliczający średnią wartość z podanych przez użytkownika liczba. Do przechowywania liczb użyj listy. Pozwól na wprowadzenie maksymalnie 10 liczb.
Skorzystaj z funkcji wbudowanej sum().

### Pętla for

#### Zadanie 

Napisz program zliczający wystąpienia liczb dodatnich i ujemnych w zadanej liście liczb całkowitych.

#### Zadanie

Napisz program wypisujący wszystkie libczy od 0 do 100, podzielne przez 3 lub podzielne przez 5. Wypisz także jak dużo takich liczb wystąpiło w tym przedziale.
Liczby podzielne przez 3 lub 5:
0
3
5 ... 96 99
W przedziale 0-100 jest 48 liczb podzielnych przez
3 lub 5

#### Zadanie 

Napisz program wypisujący na konsolę tabliczkę mnożenia dla liczb od 0 do 9 w postaci tabelki.

           0    1    2    3    4    5    6    7    8    9
    
    0      0    0    0    0    0    0    0    0    0    0
    1      0    1    2    3    4    5    6    7    8    9
    2      0    2    4    6    8   10   12   14   16   18
    3      0    3    6    9   12   15   18   21   24   27
    4      0    4    8   12   16   20   24   28   32   36
    5      0    5   10   15   20   25   30   35   40   45
    6      0    6   12   18   24   30   36   42   48   54
    7      0    7   14   21   28   35   42   49   56   63
    8      0    8   16   24   32   40   48   56   64   72
    9      0    9   18   27   36   45   54   63   72   81

#### Zadanie

Napisz program zamieniający miejscami w zadanej liści liczb element największy z najmniejszym.

### Napisy

#### Zadanie

Napisz program zliczający liczbę wystąpień samogłosek (a, e, i, o, u, y) w podanym przez użytkownika napisie.

#### Zadanie

Napisz program zliczający liczbę znaków w podanym przez użytkownika napisie pomiędzy nawiasami <>. Nawiasy mogę wystąpić tylko raz.

    Ala ma <kota>, a kot ma Alę
    4

### Słownik

#### Zadanie

Napisz program zliczający liczbę wystąpień każdego znaku w podanym przez użytkownika napisie.

#### Zadanie (opcjonalne)

Napisz program wyliczający kwotę należną za zakupiony towar na podstawie podanej przez użytkownika wagi i nazwy produktu. Do przechowywania informacji o cenie za kilogram danego produktu użyj słownika. Wypisz wszystkie dostępne produkty w sklepie.

### Zbiór

- suma-|
- różnica - -
- iloczyn - &
- różnica symetryczna - ˆ

#### Zadanie

Napisz program zliczający liczbę unikalnych liczb wprowadzonych przez użytkownika. Sprawdź jak dużo z tych liczb jest liczbami parzystymi w zakresie 0-100 - w tym celu skorzystaj z operatora iloczynu.

### Utrwalenie

#### Zadanie

Napisz program, który posortuje liczby w tablicy przy wykorzystaniu algorytmu “sortowanie przez wybieranie”.

### Wyrażenia listowe i inne

W sesji interaktywnego środowiska stwórz następujące struktury danych korzystając ze skróconej wersji zapisu:
- listę zawierającą liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1
- zbiór tupli zawierających 3 elementy - daną liczbę, jej kwadrat i jej sześcian - w przedziale od -10 do 10
- słownik mapujący napisy na ich długość powstały ze zbioru napisów

## Funkcje

### Argumenty pozycyjne

#### Zadanie

Napisz funkcję sprawdzającą, czy dane liczba jest liczbą pierwszą. Przykład użycia:

    >>> czy_jest_pierwsza(10)
    False
    >>> czy_jest_pierwsza(17)
    True

#### Zadanie

Napisz funkcję zwracającą zbiór wszystkich znaków występujących w napisie więcej niż zadana liczba razy.
Przykład użycia:

    >>> wiecej_niz('ala ma kota a kot ma ale', 3)
    {'a', ' '}

### Argumenty nazwane

Napisz funkcję obliczającą liczbę znaków w zadanym napisie pomiędzy zadanymi znakami. Znaki, pomiędzy którymi ma odbywać się zliczanie, powinny być argumentami z wartościami domyślnymi - odpowiednio < i >. Nawiasy mogę być zagnieżdżone i mogą wystąpić wiele razy. Znaki pomiędzy zagnieżdżonymi nawiasami liczone są zgodnie z poziomem zagnieżdżenia.
Przykład użycia:

    >>> policz_znaki('ala ma <kota> a kot ma ale')
    4
    >>> policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']')
    18
    >>> policz_znaki('a <a<a<a>>>')
    6

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

Zaimplementuj zestaw dekoratorów otaczających zwracany przez funkcję napis tagami HTML (pogrubienie, podkreślenie, przekreślenie):
Przykład użycia:

    @bold
    @italic
    def foo(arg):
        return f'To jest {arg}' 

#### Zadanie

Zaimplementuj dekorator wypisujący wywołanie danej funkcji (nazwa i argumenty) oraz czas jej wykonania.
Przykład użycia:

    @log
    def foo(arg):
        return f'To jest {arg}'


## Klasy

### Atrybut klasowy

### Atrybut instancji (metoda __init__)

#### Zadanie

Zaimplementuj klasę Product przechowującą informację o cenie, nazwie oraz ID produktu. Zaimplementuj metodę wypisującą informację o produkcie na konsolę.
Przykład użycia:

    >>> product = Product(1, 'Woda', 10.99)
    >>> product.print_info()
    Produkt "Woda", id: 1, cena: 10.99 PLN

#### Zadanie

Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu pracy oraz wypłacanie pensji na podstawie zadanej stawki godzinowej. Jeżeli pracownik będzie pracował więcej niż 8 godzin (podczas pojedynczej rejestracji czasu) to kolejne godziny policz jako nadgodziny (z podwójną stawką godzinową).
Przykład użycia:

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

Zaimplementuj klasę CashMachine umożliwiającą wpłacanie i wypłacanie pieniędzy. 
Zadbaj o to aby stan bankomatu przetrzymywany był w zmiennych prywatnych.
Przykład użycia:

    >>> cash_machine = CashMachine()
    >>> cash_machine.is_available
    False
    >>> cash_machine.put_money([200, 100, 100, 50])
    >>> cash_machine.is_available
    True
    >>> cash_machine.withdraw_money(150)
    [100, 50]

#### Zadanie 

Zaimplementuj klasę ElectricCar odwzorowującą zachowanie samochodu elektrycznego. Klasa powinna umożliwiać pokonanie zadanego dystansu, który nie może przekroczyć maksymalnego zasięgu zdefiniowanego dla samochodu. Samochód powinien mieć także możliwość naładowania baterii.

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

Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora swobodnego na dwuwymiarowej płaszczyźnie. 
Wektory powinny mieć możliwość dodawania, odejmowania, mnożenia (przez inny wektor i przez liczbę), porównywania (po długości) oraz powinny posiadać czytelną reprezentację napisową.
Przykład użycia:

    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1 + vector_2