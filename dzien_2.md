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

