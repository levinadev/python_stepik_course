"""
Дан словарь: country = {"name": "Россия", "capital": "Москва", "population": 146000000}.
Используя метод .items(), выведите все пары ключ-значение в формате:
"Ключ: {key}, Значение: {value}" (каждая пара на отдельной строке).
"""

country = {"name": "Россия", "capital": "Москва", "population": 146000000}

for key, value in country.items():
    print(f"Ключ: {key}, Значение: {value}")