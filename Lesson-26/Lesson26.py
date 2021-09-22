#Klasy, dziedziczenie

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal): #w nawiasie piszemy klasę po której dziedziczymy
    def voice(self):
        print("How How")

dog = Dog("Reksio", 10)
print(dog.name)
print(dog.age)
dog.voice() #tutaj nie trzaba print(), bo funkcja voice już ma print

class Cat(Animal):
    def getVoice(self):
        print("Meow Meow")

cat = Cat("Bury", 8)
cat.getVoice()

class Wolf(Dog):
    def getVoice(self):
        print("Jestem wilkiem, ")
        super().voice() # super podobne do self

wolf = Wolf("Geralt", 55)
wolf.getVoice()