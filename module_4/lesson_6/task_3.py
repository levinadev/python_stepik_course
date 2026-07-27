"""
Создайте класс Product с:
Конструктором, принимающим название (name) и цену (price).

Методом __add__, который складывает цены двух товаров и возвращает сумму.

Создайте два товара:
product1 = Product("Ноутбук", 75000)
product2 = Product("Мышь", 1500)

Выведите результат сложения product1 + product2.
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __add__(self, other):
        return self.price + other.price

product1 = Product("Ноутбук", 75000)
product2 = Product("Мышь", 1500)
print(product1 + product2)