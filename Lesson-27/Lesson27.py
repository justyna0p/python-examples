#Klasy i magiczne metody

import math #dzięki temu mamy funkcje pierwiasta .sqrt

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = math.sqrt(x**2 + y**2)

    def __add__(self, second): #aby móc dodać dwa punkty do siebie (p1 i p2)
        return Point2D(self.x + second.x, self.y + second.y)

    def __lt__(self, second):
        return self.distance < second.distance

    def __eq__(self, second):
        return self.x == second.x and self.y == second.y

    def __len__(self):
        return int(round(self.distance, 0))

p1 = Point2D(2, 5)
p2 = Point2D(4, 5)
p3 = p1 + p2
print(p3.x)
print(p3.y)
print(p1.distance)
print(p2.distance)
print(p3 < p2)
print(p1 == p2)
print(p2 == p2)
print(len(p3))
print(p3.distance)