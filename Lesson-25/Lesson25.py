#Klasy i obiekty

#Klasy
#Nazwy klas z dużej litery. Funkcja wewnątrz klasy to metoda.
#Klasy pozwalają na stworzenie szablonu, którym posłużymy się do stworzenia obiektu
#Self - nazwa pierwszego predefiniowanego argumentu - jest argumentem specjalnym (może być inna nazwa np abc)

#Tworzenie obiektu pierwszego na danej klasie
class Human: #klasa
    name = "Sebastian" #zmienna
    def introduceYourself(self): #funkcja czyli metoda
        return "Hello, my name is " + self.name
object = Human()
print(object.name)
print(object.introduceYourself())

#Tworzenie nowego obiektu na tej samej klasie
object1 = Human()
object1.name = "Adrian"
print(object1.introduceYourself())


#Modyfikacja klasy o specjalną metodę __init__ - pobieranie danych bezpośrednio z konstruktora
class Human2:
    def __init__(self, name2, age2):
        self.name2 = name2
        self.age2 = age2
    def introduceYourself2(self, welcome = "Hello"):
        return welcome + ", my name is " + self.name2 + " and I have " + str(self.age2) + " years old."

object = Human2("Mikołaj", 24)
print(object.introduceYourself2("Hi"))

#Tworzenie nowego obiektu na tej samej klasie
object2 = Human2("Kamil", 18)
print(object2.introduceYourself2())

