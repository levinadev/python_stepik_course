"""
Создайте класс Square с:
Конструктором, принимающим сторону (side).
Методом area(), который возвращает площадь квадрата (side * side).

Создайте класс Triangle с:
Конструктором, принимающим основание (base) и высоту (height).
Методом area(), который возвращает площадь треугольника (base * height / 2).

Создайте список figures = [Square(4), Triangle(6, 3)].
В цикле вызовите метод area() для каждого объекта и выведите результат на отдельной строке.
"""

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2


figures = [Square(4), Triangle(6, 3)]

for figure in figures:
    print(figure.area())