#łączenie elementów listy - .join
print(", ".join(["a", "b", "c"]))

#Zmiana elementu w tekście - .replace
print("Hello Świecie".replace("Hello", "Hi"))

#Czy zdanie rozpoczyna się od...? zwraca wartość T/F - .stratswith
print("This is a sentence".startswith("this")) #wielkość liter ma znaczenie (this!=This)

#Czy zdanie kończy się na...? zwraca wartość T/F - .endswith
print("This is a sentence".endswith("e"))

#Szukanie wartości w wyrażeniu. Zwraca wartość T/F - in
print("s" in "This is a sentence.")

#Wielkie litery - .upper
print("This is a sentence.".upper())

#Małe litery - .lower
print("This IS a sENTENCe.".lower())

print("------")

#Funkcja all - każdy element z listy musi spełnić warunki, żeby funkcja zadziałała
list1 = [10, 20, 25, 35, 40]

if all([i % 2 == 0 for i in list1]): #sprawdzzamy czy liczby są parzyste w liście
    print("All numbers are even")

#Funkcja any - wykona się jeśli chociaż jeden element z listy spełni warunek
if any(i % 2 == 0 for i in list1):
    print("At least one number is even")

#Wypisanie elementów listy
for i in list1:
    print(i)

#Numerowanie elementów listy - krotka
for i in enumerate(list1):
    print(i)

#Numerowanie elementów w czytelny sposób. Sposób 1
for i in enumerate(list1):
    print(i[0] + 1, "-", i[1])
print("------------\n")

#Numerowanie elementów w czytelny sposób. Sposób 2
for i, element in enumerate(list1):
    print(i + 1, "-", element)