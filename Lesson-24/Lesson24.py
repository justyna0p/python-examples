#Zbiory - operacje na zbiorach

numbers1 ={0, 1, 2,  4} #{} - zbiór w nawiasach w klamrach
words = set(["a", "b", "c"]) #z listy przechodzimy w zbiór dzięki funkcji set

print(numbers1)
print(words)

#Dodawanie do zbioru
numbers1.add(5)
print(numbers1)

#Usuwanie ze zbioru
numbers1.remove(0)
print(numbers1)

#Inne funkcje
#.pop() - zdejmuje pierwszy element ze zbioru
#.clear() - czyści cały zbiór

#W zbiorach elementy się nie powtarzają
numbers3 = {0, 1, 2, 4, 4, 5, 5, 5}
print(numbers3)

#Szukanie elementu w zbiorze
print("a" in numbers1) #true/false czy "a" jest w zbiorze numbers1?

#Zbiory do zadań
numbers1 ={0, 1, 2, 3, 4} #nadpisujemy
numbers2 = {3, 4, 5, 6}

#Suma zbiorów
print(numbers1 | numbers2) #wyświetla wszystkie liczby zawarte w obu zbiorach

#Iloczyn zbiorów
print(numbers1 & numbers2) #iloczyn, dana wartość musi być w obu zbiorach

#Różnica zbiorów - kolejność ma znaczenie
print(numbers1 - numbers2)
print(numbers2 - numbers1)

#Różnica symetryczna
print(numbers1 ^ numbers2)
#Odejmujemy z obu zbiorów to co się w nich powtarza, z pozostałych liczb tworzymy jeden zbiór

