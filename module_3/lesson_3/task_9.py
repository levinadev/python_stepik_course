"""
Дан список: numbers = [1, 2, 3, 4, -5].
Используя any() и all():

Проверьте, есть ли в списке хотя бы одно отрицательное число (any).

Проверьте, все ли числа положительные (all).
Выведите результаты в формате: "Есть отрицательное: {True/False}" и "Все положительные: {True/False}".
"""

numbers = [1, 2, 3, 4, -5]
has_negative = any(x < 0 for x in numbers)
all_positive = all(x > 0 for x in numbers)
print(f"Есть отрицательное: {has_negative}")
print(f"Все положительные: {all_positive}")