dictionary = {1: "Monday", 2: "Tuesday", 7: "Sunday"} #1-klucz: "Monday" wartość dla klucza, objaśnienie. Mamy trzy pary wartości

print(dictionary[1])
print(dictionary[7])

#dodawanie wartości do słownika - na sam koniec
dictionary[3] = "Wednesday"

#słownik nie musi mieć jednogo typu wartości
dictionary[4] = False
dictionary[5] = 5
print(dictionary)

#słownik nie musi mieć jednego typu kluczy
dictionary["a"] = 1
print(dictionary["a"])
print(dictionary)

#wyświetlanie nieistniejących wartości
#print(slownik[8]) #wyświetlanie wartości której nie ma - nie ma wartości o kluczu 8 - KeyError
print(dictionary.get(8, "other day"))

#wyświetlanie wartości słownika linijka po linijce
print("\nLoop:")
for l in dictionary.values():
    print(l)

print("\n---------")

#usuwanie wartości ze słownika
print(dictionary.pop(1)) #usuwanie wartości która jest pod kluczem 1 - Monday
print(dictionary)