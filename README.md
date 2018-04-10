# Tic-Tac-Toe

[![Build Status](https://travis-ci.org/pite2018-galat-bieda/Tic-Tac-Toe.svg?branch=master)](https://travis-ci.org/pite2018-galat-bieda/Tic-Tac-Toe)

Tic Tac Toe game 

# Installing:
Enter the following commands on different consoles:
python3 server.py
python3 client.py
python3 client.py

# Code review 

Do wersji samej gry, bez serwera i kienta (odpowiednia wersja w release)

Kod nie posiada dokumentacji, jednak same nazwy klas, funkcji oraz zmiennych są na tyle znaczące, iż dokumentacja nie jest wymagana. Kod napisany w zwięzły, a także zrozumiały sposób. Gra działa bezbłędnie oraz zgodnie z przeznaczeniem. README zawiera instrukcje dotyczące uruchomienia programu.

Dane wejściowe podawane przez użytkowników są sprawdzane pod względem poprawności. W przypadku podania wartości niecałkowitej rzucany jest wyjątek i pojawiają się odpowiednie komunikaty. Jednak brakuje komunikatu podczas podania wartości całkowitej innej, niż ze zbioru {0,1,2} - można dodać komunikat: "wymagana liczba całkowita z przedziału [0,2]" - aby użytkownik wiedział, jaki błąd popełnił.

Kod jest podzielony na klasy i funkcje, które wykonują oddzielne operacje.
W klasie odpowiedzialnej za widok, ciekawe rozwiązanie w funkcji clear_screan, która czyści ekran konsoli przy każdym ruchu.

W funkcji check_win podczas sprawdzania warunków wygranej można ograniczyć ilość kodu.

Testy jednostkowe szczegółowo sprawdzają, czy poszczególne funkcje są poprawnie wykonywane.
Sprawdzają, co dzieje się, gdy podane przez użytkownika pole jest zajęte, lub zostanie wybrane pole o złych wartościach — nie z przedziału [0-2][0-2], lub czy przy odpowiednim ustawianiu tablicy zadziałają w poprawny sposób warunki sprawdzające wygraną. Dodatkowo można sprawdzić, czy podczas podania złej wartości float, czy String funkcja take_number_from_user zadziała w poprawny sposób — odpowiednie komunikaty.

Jeśli chodzi o optymalizację, nie widzę żadnego powodu do zmian — funkcje są zwięzłe, kod nie powtarza się.
