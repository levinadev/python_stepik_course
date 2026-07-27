"""
Напишите программу, которая считывает целое число n и выводит сумму всех чисел от 1 до n включительно.
"""

n = int(input())
total = 0

for i in range(1, n + 1):
    total = total + i

print(total)
