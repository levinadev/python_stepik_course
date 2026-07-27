"""
Напишите функцию max_of_two(a, b), которая принимает два числа и возвращает большее из них.
Считайте два числа с клавиатуры, вызовите функцию и выведите результат.
"""

input_a = int(input())
input_b = int(input())

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

print(max_of_two(input_a, input_b))