"""
Дан список numbers = [10, -5, 0, 3, -1, 7].
Используя filter() и lambda, оставьте только положительные числа (больше 0) и выведите результат.
"""

numbers = [10, -5, 0, 3, -1, 7]
result = list(filter(lambda x: x > 0, numbers))
print(result)