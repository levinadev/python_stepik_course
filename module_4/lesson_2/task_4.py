"""
Создайте класс Car, который:
В конструкторе принимает марку (brand) и модель (model).
Имеет метод info(), который выводит строку: "Машина: {brand} {model}".
Создайте объект Car("Toyota", "Camry") и вызовите метод info().
"""

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"Машина: {self.brand} {self.model}")


car = Car("Toyota", "Camry")
car.info()
