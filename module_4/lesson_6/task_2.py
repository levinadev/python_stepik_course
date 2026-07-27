"""
Создайте класс Product с:
Конструктором, принимающим название (name) и цену (price).
Методом __eq__, который сравнивает два товара по названию и цене.

Создайте два объекта:
product1 = Product("Телефон", 30000)
product2 = Product("Телефон", 30000)
Выведите результат сравнения product1 == product2.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price


product1 = Product("Телефон", 30000)
product2 = Product("Телефон", 30000)
print(product1 == product2)