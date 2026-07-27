"""
Дан список numbers = [1, 2, 3, 4, 5].
Используя map() и lambda, преобразуйте все числа в их квадраты и выведите результат.
"""

numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x ** 2, numbers))
print(result)