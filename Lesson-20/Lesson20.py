#Funckje anonimowe - lambda

#Jedna zmienna
def function(f, number):
    return f(number)
print(function(lambda x: x * x, 3))

def square(x):
    return x * x
print(square(5))

result = (lambda x: x * x)(5)
print(result)

lam = lambda x: x * x
print(lam(5))
print(lam(3))

lam2 = lambda x, y: x * y
print(lam2(2, 3))

print((lambda x, y: x + y)(5, 6))