#Otwieranie pliku źódłowego
plik = open("tekst.txt", "r")
text = plik.read() #wczytywanie tekstu to zmiennej tekst
plik.close() #zamykamy plik aby zwolnić pamięć

#ile razy dana litera występuje w tekście
def count(txt, sign):
    meter = 0
    for z in txt:
        if z == sign:
            meter += 1
    return meter
print(count(text, "A") + count(text, "a"))
print(count(text.lower(), "a"))


#analiza wszystkich liter jednocześnie z ilością procentowego udziału w danym tekście
for z in "abcdefghijklmnoprstuwxyz": #"abc..." stowrzenie listy z alfabetem
    hm = count(text.lower(), z)
    percent = 100 * hm / len(text)
    print("{0} - {1} - {2}%".format(z.upper(), hm, round(percent, 2))) #formater 0-litera, 1-liczba wystąpień, 2- procent

    #print(f"{z.upper()} - {hm} - {round(percent, 2)}%") - to samo co wyżej przy zastosowanie f formatter