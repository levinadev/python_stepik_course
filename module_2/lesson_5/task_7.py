"""
Дан словарь: product = {"title": "Ноутбук", "price": 75000, "brand": "Asus"}.
Используя метод .get(), получите значение ключа "price".
Затем получите значение ключа "discount" со значением по умолчанию 0.
Выведите оба значения в формате: "Цена: {price}, Скидка: {discount}"
"""

product = {"title": "Ноутбук", "price": 75000, "brand": "Asus"}
price = product.get("price")
discount = product.get("discount", 0)
print(f"Цена: {price}, Скидка: {discount}")