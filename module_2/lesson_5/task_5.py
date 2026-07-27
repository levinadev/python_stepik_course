"""
Дан словарь: student = {"name": "Иван", "age": 20, "group": "A-101", "faculty": "Математический"}.
Используя метод .values(), выведите все значения словаря, каждое на отдельной строке.
"""

student = {"name": "Иван", "age": 20, "group": "A-101", "faculty": "Математический"}

for value in student.values():
    print(value)