#obsługiwanie błędów nie przerywając programu
def division1 (x, y):
    if y == 0:
        raise ZeroDivisionError("Dzielenie przez 0")
    print( x / y)

try:
    division1(2, 0)
except ZeroDivisionError:
    print("Błąd")

#Assert przerywa program, jeśli będzie błąd

def division2 (x, y):
    assert y != 0, "Y == 0"
    if y == 0:
        raise ZeroDivisionError("Dzielenie przez 0")
    print( x / y)

try:
    division2(2, 0)
except ZeroDivisionError:
    print("Błąd")
    raise