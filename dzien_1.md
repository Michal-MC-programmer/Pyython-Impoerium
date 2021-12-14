# WSTĘP

## Zasady
- poufność
- telefony odbieramy na zewnątrz
- pytania zadajemy od razu
- pytania merytoryczne zadajemy głośno
- pomagamy sobie nawzajem
- staramy się możliwie zredukować problemy pracowe


## Ogólne informacje o programowaniu

- jak powstaje i działa program? 
- języki programowania
    - język maszynowy
    - assembler
    - języki wyższego poziomy
        - kompilowane
        - interpretowane

- konsola systemowa
    - uruchamianie 
    - wydawanie polecen (dir, mkdir)

## Język Python

- krótka historia
- instalacja
  - interpreter języka
  - wirtualne środowisko
  
## Środowisko

- Edytory
- IDE
- pycharm
- git


## Podstawowe typy danych

### liczby całkowite ‐ int

### liczby zmiennoprzecinkowe - float

### Operatory arytmetyczne

- operator dodawania ‐ +
- operator odejmowania ‐ ‐
- operator mnożenia ‐ *
- operator dzielenia ‐ /
- operator dzielenia całkowitoliczbowego ‐ // 
- operator modulo (reszta z dzielenia) ‐ % 
- operator potęgi ‐ **

#### Zadanie

W sesji interaktywnego środowiska interpretera oblicz następujące wartości:
- pole trójkąta o podstawie 10 i wysokości 5
- pole koła o promieniu 7
- pole trapezu o długości podstaw 3 i 9 oraz wysokości 6.5 objętość kuli o promieniu 7/8

### wartości logiczne ‐ bool

#### Operatory porównania

- operator równości ‐ ==
- operator różny od ‐ !=
- operator mniejsze od ‐ <
- operator mniejsze od lub równe ‐ <= operator większe od ‐ >
- operator większe od lub równe ‐ >=

#### Operatory logiczne

- operator koniunkcji ‐ and 
- operator alternatywy ‐ or 
- operator negacji ‐ not

### napisy ‐ str 

### Funkcja help

### Funkcja dir

## programy w module

### Uruchomienie programu

### Funkcja print

### Funkcja input

### zmienne

#### Zasady nazewnictwa

#### Zadanie

Korzystając z przypisywania wartości do zmiennych napisz program obliczający pole trapezu o długości podstaw 3 i 9 oraz wysokości 6.5.

#### Zadanie 

Napisz program wypisujący na konsolę Twoje imię i wzrost. Do przechowywania informacji o Twoim imieniu i wzroście użyj zmiennych.
Przykładowy komunikat programu:

    Imię: Jan
    Wzrost: 180

#### Zadanie

Napisz program wyliczający kwotę należną za zakupiony towar na podstawie ceny za kilogram oraz liczby zakupionych kilogramów. 
Do przechowywania informacji o cenie oraz liczbie kilogramów użyj zmiennych. Wypisz wszystkie informacj na konsolę.
Przykładowy komunikat programu:

    Cena za kg: 10.0
    Waga: 2.5
    Należność: 25.0

#### Zadanie

Napisz program obliczający koszt przejazdu z miasta A do B na podstawie podanej przez użytkownika liczby kilometrów, 
ceny paliwa oraz spalania. Zapytaj użytkownika także o nazwy miejscowości.
Przykładowe komunikat programu:

     Miasto A: Warszawa
     Miasto B: Gdańsk
     Dystans Warszawa‐Gdańsk: 420
     Cena paliwa: 4.55
     Spalanie na 100 km: 5.5
     Koszt przejazdu Warszawa‐Gdańsk to 105 PLN
 
#### Zadanie

Napisz program sprawdzający czy podana przez użytkownika liczba jest:
- większa od 10
- mniejsza równa 15
- podzielna przez 2 (użyj operator modulo)

Przykładowy komunikat programu:

     Podaj liczbę: 15
     Większa od 10: True
     Mniejsza równa 15: True
     Podzielna przez 2: False


#### Zadanie

Napisz program sprawdzający czy podana przez użytkownika liczba jest podzielna przez 2, 
podzielna przez 3 i większa od 10 lub jest to liczba 7.

### instrukcja warunkowa if 

#### Zadanie

Napisz program, który sprawdzi pełnoletność osoby na podstawie roku jej urodzenia.
Przykładowy komunikat programu:
    
    Podaj rok urodzenia: 1980
    Jesteś pełnoletni!

#### Zadanie

Napisz program, który na podstawie dwóch podanych liczb obliczy wynik zadanej operacji (dodawanie, odejmowanie, mnożenie, dzielenie). W przypadku podania nieprawidłowej operacji program ma wyświetlić odpowiedni komunikat błędu.
Przykładowy komunikat programu:

     Podaj pierwszą liczbę: 10
     Podaj drugą liczbę: 5
     Podaj rodzaj operacji: +
     Wynik: 15
 
#### Zadanie

Napisz program, który na podstawie pozycji gracza (x, y) na planszy w przedziale od 0 do 100 wyświetli jego przybliżone położenie (centrum, prawy górny róg, górna krawędź, ...) lub informację o pozycji poza planszą. Przyjmij wartość 10 jako margines krawędzi.
Przykładowy komunikat programu:

     Podaj pozycję gracza X: 95
     Podaj pozycję gracza Y: 95
     Gracz znajduje się w prawym górnym rogu.


### pętla while
 
#### Zadanie

Napisz program obliczający kwadrat 100 pierwszych liczba całkowitych i wypisujący wyniki na konsolę.

#### Zadanie

Napisz program obliczający średnią wartość temperatury w danym tygodniu na podstawie temperatur wprowadzonych przez użytkownika.

#### Zadanie

Napisz program wyświetlający minimalną oraz maksymalną liczbę z wszystkich liczb wprowadzonych przez użytkownika. Daj użytkownikowi możliwość zakończenia wprowadzania liczb odpowiednią komendą. 
Zadbaj o obsłużenie przypadku gdy użytkownik nie wprowadzi żadnej liczby.

#### Zadanie (opcjonalnie)

Napisz grę polegającą na poszukiwaniu skarbu na dwuwymiarowej planszy o rozmiarach 10 na 10. 
Użytkownik może wprowadzać komendy zmieniające położenie postaci. 
Po każdym ruchu użytkownik powinien otrzymywać informację o tym czy zmierza dobrym kierunku. 
Wyjcie poza planszę oznacza koniec gry. Po znalezieniu skarbu wypisz liczbę ruchów wykorzystanych przez użytkownika na dojście do celu.
Dodatkowo:
po wykonaniu większej liczby kroków niż minimalna wartość x 2, umieść skarb w nowym miejscu
z prawdopodobieństwem 1/5 nie podawaj graczowi wskazówki po wykonaniu kroku

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