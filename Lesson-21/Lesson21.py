#Mapa działa jak return. Wykonuje się na pewnej funkcji (co ma robić) i na kolekcji (lista argumentów na którą ma działać)
#Filtry w odróżnieniu od mapy zwraca T/F, filtry wybierają nam tylko pożądane wartości z listy

numbers = [2, 10, 12, 15, 20, 25, 30, 35]

#Mapy
def function(x):
    return x * 2

result = map(function, numbers)
print(list(result))

result2 = map(lambda x: x + 2, numbers) #zamiast zdeklarowanej funkcji, można napisać ją samemu - lambdą
print(list(result2))

#Filtry
result3 = filter(lambda x: x % 2 == 0, numbers)
print(list(result3))