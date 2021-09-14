lista = ["Subskrybuj", "Kanał", "o", "Wszystkim"]

i = 0
while i < len(lista):
    print(lista[i])
    i += 1

for x in lista: #x-deklaracja nowej zmiennej (może być pusta), będzie przyjmowała argumenty z kolekcji
    print(x)

print(range(10)) #funkcja range przechowuje kolekcje
print(list(range(10))) #konwertujemy (przerzutować na listę) na typ listy -> tworzy się tabela z 10 elementami od 0 do 9

for y in range(10): #pętla wykona się 10 razy
    print(y)

for y in range(10):
    print(y+1)

for z in range(1, 11):
    print(z)

for m in range(0, 22, 3): #możemy dodać trzeci argument i on mówi nam o skoku. Czyli o ile elementów chcemy przeskakiwać w naszej kolekcji
    print(m)