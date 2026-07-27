"""
Дан словарь: city = {"name": "Москва", "population": 12000000, "country": "Россия"}.
Выполните действия:
Добавьте ключ "mayor" со значением "Собянин".
Удалите ключ "population" с помощью del.
Выведите итоговый словарь.
"""

city = {"name": "Москва", "population": 12000000, "country": "Россия"}
city["mayor"] = "Собянин"
del city["population"]
print(city)