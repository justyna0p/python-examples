#Generatory - yield
#yield zastępuje return - zwraca wartość, ale nie przerywa po podaniu jednej wartości (jak return), bo jest to pętla

#Funkcja
def gen():
    i = 0
    while i < 5:
        yield i
        i += 1 # pętla wykona się 5 razy. Od 0 do 4

#Iterowanie poprzez pętle for
for i in gen(): # to ma sens tylko gdy funckja jest generatorem, czyli ma yield zamiast return
    print(i)

#Przedstawienie wyniku za pomocą listy
print(list(gen()))

#Kolejny przykład - liczby parzyste
def even(x):
    i = 0
    while i <= x:
        if i % 2 == 0:
            yield i
        i += 1
for i in even(16):
    print(i)
print(list(even(16)))