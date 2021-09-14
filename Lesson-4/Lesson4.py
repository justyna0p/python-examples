#hierarchia and>or
# false and false -> false; true or false -> true
if True or False and False:
    print('Prawda')
else:
    print("Fałsz")

# true or false -> true; true and false -> false
if (True or False) and False:
    print("Fałsz")
else:
    print("Prawda")

#Zadanie: film dla dorosłych w kinie. Bilet kosztuje 35zł
age = 19
money = 30
if age >= 18 and money >= 35:
    print("Możesz wejść")
else:
    print("Nie możesz wejść")

#Zadanie: Film w kinie. Do 12 roku życia wejście za darmo. Powyżej 12 roku życia film kosztuje 30zł.
age = 19
money = 30
if age <= 12 or money >= 30:
    print("Możesz wejść")
else:
    print("Nie możesz wejść")