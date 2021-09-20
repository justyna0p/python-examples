#Wyrażenie listowe pozwalają nam działać na każdym elemencie listy. Co innego niż wycinek, który zwraca część listy, jakiś zbiór.
#Wyrażenie listowe zwracają całą kolekcję i można przeprowadzać operacje na zbiorze argumentów listy.

list1 = list(range(10))
print(list1)

#Mnożenie wszystkich elementów
new = [i * 2 for i in list1] #każdy argument mnożymy razy 2
print(new)

#Dodawanie
new2 = [i + 2 for i in list1 if i % 2 == 0] #dodaj wartość 2 do liczb parzystych, l.nieparzyste zostały pominięte
print(new2)

#Formatowanie ciągów string (string formatter)
arguments = ["Sebastian", 24]
text = "Cześć mam na imię {name} i mam {age} lata. {name}".format(name = arguments[0], age = arguments[1])
print(text)