"""
Дан список: original = ["a", "b", "c"].
Создайте его копию через метод .copy(), удалите из копии последний элемент с помощью .pop() и выведите копию.
"""

original = ["a", "b", "c"]
copy = original.copy()
copy.pop()
print(copy)