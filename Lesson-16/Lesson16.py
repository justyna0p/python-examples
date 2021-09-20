tuple = (2, 4, 8, 16, 32, 64, 128)

print(tuple)

#Zmiana danych w krotce
#błąd TypeError - tuple. Krotka nie wpsiera przepisania elementów. Pozostaja taka sama od początku do końca.
#tym się różni od listy.

#Ilość danych elementów w krotce
print("Amount of elements (2):", tuple.count(2)) #ile jesr "2" w krotce

#Szukanie wartości w krotce
print("Index (64):", tuple.index(64)) #index wartości 64

#Wycinki
print("\nWycinki:")
print(tuple[0:3]) #<0:3) od indexu 0 do 3 (bez 3) - indeks 0, 1 i 2
print(tuple[3:5]) # indexy 3 i 4
print(tuple[3:200]) #w celu wyświetlenia ostatniego elementu trzeba podać wysoki index (nieistniejący)
print(tuple[3:]) #można też drugi element zostawić pusty. Wtedy krotka wyświetli się też do samego końca
print(tuple[-4:-2]) #liczymy z lewej od 1 (nie od zera). Pamiętamy że <-4,-2)

#Skoki kolekcji
print(tuple[0:7:2]) #od pierwszego do ostatniego co drugi element

#Odwracanie kolekcji
print(tuple[::-1])