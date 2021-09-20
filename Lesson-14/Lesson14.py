#ilość znaków w tekście
plik = open("test.txt", "a")
if plik.writable(): #jeśli plik nadaje się do zapisu to wpisz poniższe:
    ile = plik.write(input("Wprowadź tekst: ") + "\n") # wprowadzanie tekstu do pliku. \n new line - od nowego wiersza
    # \n - to też jest znak
    print("Zapisano: ", ile)
plik.close() #zamknąć plik bezpośrednio. Aby zwolnić pamięć

plik = open("test.txt", "r")

if plik.readable():
    print("Zawartość pliku")
    for l in plik:
        print(l)

