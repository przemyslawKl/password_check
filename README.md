Password Validator
Prosty program w Pythonie służący do sprawdzania poprawności i siły hasła.

Funkcjonalności
Program weryfikuje czy hasło:

nie jest puste,
ma minimalną wymaganą długość,
nie zaczyna się spacją,
nie kończy się spacją,
zawiera co najmniej jedną małą literę,
zawiera co najmniej jedną wielką literę,
zawiera co najmniej jedną cyfrę,
zawiera co najmniej jeden znak specjalny.

Dodatkowo:

oblicza siłę hasła,
wyświetla szczegółowe statystyki znaków,
uruchamia zestaw testów automatycznych.
Wymagania
Python 3.8 lub nowszy

Sprawdzenie wersji:

python --version
Uruchomienie programu

Uruchom plik:

python password_validator.py
Program poprosi o podanie:

minimalnej długości hasła,
hasła do sprawdzenia.

Przykład:

Podaj minimalna dlugosc hasla (Enter = 12):
Prosze podaj haslo: Password123!
Przykładowy wynik
Hasło niepoprawne
Liczba bledow: 2

Statystyki:
Liczba znakow: 11
Male litery: 7
Wielkie litery: 1
Cyfry: 3
Znaki specjalne: 0

Sila hasla to: Mocne

Wykryto bledy:
- Brak znaku specjalnego
- Haslo musi miec co najmniej 12 znakow
Hasło poprawne
Haslo spelnia wszystkie wymagania.
Sila hasla to: Bardzo mocne

Statystyki:
Liczba znakow: 23
Male litery: 17
Wielkie litery: 2
Cyfry: 4
Znaki specjalne: 1
Ocena siły hasła
Program przyznaje punkty za spełnienie poniższych kryteriów:

Kryterium	Punkty
Minimalna długość	1
Mała litera	1
Wielka litera	1
Cyfra	1
Znak specjalny	1
Skala oceny
Punkty	Ocena
1	Bardzo słabe
2	Słabe
3	Średnie
4	Mocne
5	Bardzo mocne
Dozwolone znaki specjalne

Program rozpoznaje następujące znaki specjalne:

! @ # $ % ^ & *
Statystyki hasła
Program zlicza:

liczbę wszystkich znaków,
liczbę małych liter,
liczbę wielkich liter,
liczbę cyfr,
liczbę znaków specjalnych.
Przykład:

Statystyki:
Liczba znakow: 15
Male litery: 8
Wielkie litery: 2
Cyfry: 4
Znaki specjalne: 1

Testy automatyczne
W programie znajdują się przykładowe przypadki testowe:

Puste hasło
Za krótkie hasło
Brak wielkiej litery
Brak cyfry
Brak znaku specjalnego
Spacje na początku lub końcu
Poprawne hasło
Po uruchomieniu programu testy są wykonywane automatycznie.

Struktura programu

Funkcja główna
validate_password(password, min_length)
Zwracane wartości
is_valid
problems
strength
stats
Opis:

is_valid - informacja czy hasło spełnia wymagania,
problems - lista wykrytych błędów,
strength - ocena siły hasła,
stats - słownik zawierający statystyki.

Możliwe rozszerzenia

Projekt można rozbudować o:

obsługę większej liczby znaków specjalnych,
generowanie losowych haseł,
zapis raportów do pliku,
interfejs graficzny (Tkinter),
testy jednostkowe (unittest lub pytest),
sprawdzanie haseł przeciwko popularnym słownikom.

Autor
Projekt edukacyjny stworzony w celu nauki:

funkcji,
pętli,
warunków,
słowników,
walidacji danych,
pracy na ciągach znaków w Pythonie.