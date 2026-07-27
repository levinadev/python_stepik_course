"""
Даны два списка: letters = ["a", "b", "c", "d"] и numbers = [1, 2, 3].
Используя zip(), выведите пары в формате: "{letter}: {number}".
"""

letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3]

for letter, number in zip(letters, numbers):
    print(f"{letter}: {number}")