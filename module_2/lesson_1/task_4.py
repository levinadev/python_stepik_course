"""
Дан список letters = ['a', 'c', 'd'].
Вставьте букву 'b' на позицию 1 (между 'a' и 'c') с помощью .insert().
Удалите букву 'd' с помощью .remove().
Выведите итоговый список.
"""

letters = ['a', 'c', 'd']
letters.insert(1, 'b')
letters.remove('d')
print(letters)