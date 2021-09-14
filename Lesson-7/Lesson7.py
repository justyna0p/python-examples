#wyświetlanie elementów listy. Ideksujemy od 0
list1 = [1, 2, "c", "d", "e"]
print(list1)
print(list1[0]) #wyświetlanie 1. elementu listy

#zagnieżdzenie listy w liście i wywoływanie
list2 = [1, 2, 3, "d", "e", "f", ["g", "h"]]
print(list2[6][1]) #wyświetlenie 2. argumentu z zagnieżdżonej listy w argumencie 7.

#zmiana elementu w liście
list3 = [1, 2, 3, "a", "b", "c"]
print(list3)
list3[2] = "d"
print(list3)

#dodawanie do listy elementy i inne listy metodą .append (na koniec listy)
list4 = [1, 2, 3, 4, 5, "a"]
print(list4)
list4.append("b") #dodaje element
print(list4)
list4.append(["c", "d"]) #dodaje listę
print(list4)

#dodawanie do listy elementy i inne listy metodą insert (w dowolnym miejscu)
list5 = ["a", "b", "c"]
print(list5)
list5.insert(0, 1) #dodaje element "1" jako pierwszy element
print(list5)

#mnożenie listy
list6 = ["x", "y", 1]
print(list6)
print(list6 * 3) #lista miała 3 argumenty, teraz będzie miała 3*3=9 argumentów
print(list6)

#wyświetlanie ilości elementów listy
list7 = [1, 2, "a", "b", ["c", "d"]]
print(list7)
print("ilość elementów listy 7.: ", len(list7)) #zagnieżdżona lista jest jednym elementem


#wyświetlanie ilości konkretnego elementu w liście
list8 = [1, 2, 1, 1, "d", "e", [1, 2]]
print("Ilość wystąpień znaku 1 w całej liście 8.: ", list8.count(1)) #zagnieżdżona lista nie jest brana pod uwagę


#zwracanie indeksu elementu o danej wartości
list9 = [3, 1, 2, 4, 3]
print("Liczba 3 ma następujący index: ", list9.index(3)) #podajemy wartość, a komputer wyrzuca nam indexy tych wartości
#w przypadku kiedy liczba 3 jest w kilku miejscach - komputer wyrzuca nam tylko pierwszy index


#usuwanie elementów z listy
list10 = ["a", "b", "c", "f", "f", "g"]
print(list10)
list10.remove("f") #usuwanie elementu "f" z listy - tylko jednego
print(list10)
list10.remove("f") #usuwanie elementu "f" z listy - kolejne "f"
print(list10)
#nie można usunąć elementu z zagnieżdżonej listy


#wywoływanie minimalnej i maksymalnej wartości z listy
list11 = [1, 20, 35, -5, 0]
print(list11)
print("Min: ", min(list11))
print("Max: ", max(list11))


#sortowanie listy metoda .sort()
list12 = [1, 20, 35, -5, 0]
print(list12)
list12.sort()
print(list12)


#odwracanie listy metoda .reverse()
list13 = [1, 2, 3, 4, 5]
print(list13)
list13.reverse()
print(list13)


#czyszczenie listy ze wszystkich elementów metoda .clear()
list14 = ["a", "b", "c", "d", "e"]
print(list14)
list14.clear()
print(list14)

#Zadanie. Wykonać pętle while, która wypisze nam wszystkie elementy z listy (za pomocą len)

list15 = ['a', 1, 2, 3, 'b'] #5 elementowa lista, indexy od 0 do 4
x = 0
while len(list15):
    print(list15[x])
    x += 1


