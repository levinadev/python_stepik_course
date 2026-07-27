"""
📝 Итоговый проект: Система управления товарами
Условие:

Напишите программу, которая работает с каталогом товаров.

Программа должна:

Создавать товары с названием и ценой (класс Product).
Добавлять товары в корзину (класс Cart).
Выводить общую стоимость всех товаров в корзине.
Выводить информацию о каждом товаре в корзине.
Требования:

Создайте класс Product с:
Конструктором __init__(self, name, price).
Методом __str__(self), который возвращает строку в формате: "Товар: {name}, Цена: {price} руб.".
Создайте класс Cart с:
Конструктором __init__(self), который создаёт пустой список self.items для хранения товаров.
Методом add_product(self, product), который добавляет товар в корзину.
Методом get_total(self), который возвращает общую стоимость всех товаров.
Методом show_items(self), который выводит информацию о каждом товаре в корзине (каждый на отдельной строке).
Ввод:

Ввод не требуется — все данные уже заданы в коде.

Вывод:
Сначала выводится информация о каждом товаре в корзине, затем общая стоимость:

Информация о каждом товаре (каждый на отдельной строке).
Общая стоимость в формате: "Общая стоимость: {total} руб.".
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price} руб."


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def show_items(self):
        for product in self.items:
            print(product)


product1 = Product("Ноутбук", 75000)
product2 = Product("Мышь", 1500)
product3 = Product("Клавиатура", 3500)

cart = Cart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)

cart.show_items()
print(f"Общая стоимость: {cart.get_total()} руб.")