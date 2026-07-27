"""
Дан словарь: student = {"name": "Иван", "age": 20, "group": "A-101", "faculty": "Математический"}.
Используя метод .keys(), выведите все ключи словаря, каждый на отдельной строке.
"""

student = {"name": "Иван", "age": 20, "group": "A-101", "faculty": "Математический"}

for key in student.keys():
    print(key)