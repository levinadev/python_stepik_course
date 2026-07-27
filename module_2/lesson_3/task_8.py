"""
Дан вложенный список:

matrix = [
    [2, 4, 6],
    [1, 3, 5],
    [8, 10, 12]
]

Вычислите сумму всех элементов матрицы и выведите её.
"""
total = 0
matrix = [
    [2, 4, 6],
    [1, 3, 5],
    [8, 10, 12]
]

for row in matrix:
    for element in row:
        total += element

print(total)