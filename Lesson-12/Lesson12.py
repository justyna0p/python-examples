x = 12
y = 2

#ZerroDivisionError - dzielenie przez zero
#TypeError - mieszanie typów np. int i str
#IndexError - odnoszenie się do nieistniejącego elementu
try:
    lista = [3]
    print(lista[0])
    print(x + 4)
    print(x / y)
    print("Linijka po")
except (ZeroDivisionError, TypeError, IndexError):
    print("Wystąpił jeden z trzech błędów")
except: #ten wyjątek przechwyca każdy inny błąd, który nie został wspomniany wyżej
    print("Inny błąd")
finally:
    print("FINALLY: Wykonam się i tak!")


print("Dalsze instrukcje...")