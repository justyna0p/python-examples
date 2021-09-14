#mini gra. Użytkownik podaje liczbę. Musimy zgadnąć liczbę wylosowaną przez komputer. Komputer ma nam podpowiadać,
#czy wylosowana liczba jest większa, czy mniejsza od podanej przez nas liczby

from random import randint

los = randint(1,10)
odp = -1
i = 0 # zerowy obieg pętli, bo na koniec podaje ilość prób z każdym obiegiem. Dlatego nie może być 1 czy 5.
print("Zgadnij liczbę z przedziału od 1 do 10")

while odp != los:
    i += 1 #jeżeli odpowiedź różna od wylosowanej liczby, pętla się ponawia i nalicza nam kolejną próbę i
    odp = int(input("Podaj liczbę: ")) #musimy poinformować komputer, że użytkownik podaje liczbę, a nie string.
    # Określamy typ jako int -l.całkowitą
    if odp > los:
        print('Niestety wylosowana liczba jest mniejsza od Twojej')
    elif odp < los:
        print('Niestety wylosowana liczba jest większa od Twojej') #może być też drugi raz if:. Nie może być else,
        # bo ta liczba mogłaby być też równa - a więc prawidłowa.
print('Brawo! Odgadłeś za', i, "razem.")