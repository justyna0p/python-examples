#Dekorator - funkcja, której przypisujemy jedną wartość
def decorator(func):
    def wrapper():
        print("-----------")
        func()
        print("-----------")
    return wrapper()

#1. sposób
def hello():
    print("Hello World")

hello = decorator(hello) #nadpisujemy

print()

#2. sposób
@decorator
def witaj():
    print("Witaj Świecie")



