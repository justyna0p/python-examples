def function_test(): #tworzenie funkcji i jej nazwy
    print("Funkcja!") #Ciało funkcji. po wywołaniu rezultatów funkcji nie widać w konsoli, bo musimy jeszcze wywołąć funkcję

function_test() #wywoływanie funkcji po nazwie. Dopiero teraz wyświetli się ciało funkcji.

def add(x): #funkcja o nazwie dodaj z argumentem x. Argument ten istnieje tylko w tej funkcji. Jak później będzie zmienna x, to ona nam nic nie zmieni w funkcji.
    print(x + 1)

var = add(2)
print(var)

def add(x, y = 1, z = 0): #nadpisujemy pierwszą funckję, y i z - argumenty domyślne, jeśli nic nie podamy
    return x + y + z
    print("Czy ja istnieje?") #nie ma return, więc nie zadziała - dlatego w konsoli jest "None"


print(add(2, 3))
print(add(2))
result = add(2, 3, 5)
print(result)