"""
Создайте класс Product с:
Конструктором, принимающим название (name) и цену (price).
Методом __str__, который возвращает строку: "Товар: {name}, Цена: {price} руб.".

Создайте объект Product("Ноутбук", 75000) и выведите его через print().
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price} руб."


product = Product("Ноутбук", 75000)
print(product)