"""
Создайте класс Car с:

Конструктором, принимающим марку (brand).
Методом info(), который выводит: "Машина: {brand}".

Создайте класс Bicycle с:
Конструктором, принимающим марку (brand).

Методом info(), который выводит: "Велосипед: {brand}".

Создайте список vehicles = [Car("Toyota"), Bicycle("Giant")].
В цикле вызовите метод info() для каждого объекта.
"""

class Car:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(f"Машина: {self.brand}")

class Bicycle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(f"Велосипед: {self.brand}")

vehicles = [Car("Toyota"), Bicycle("Giant")]
for vehicle in vehicles:
    vehicle.info()