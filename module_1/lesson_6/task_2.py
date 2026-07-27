"""
Напишите функцию greet_user(name), которая принимает имя и выводит строку "Привет, {имя}!".
Вызовите функцию, передав имя, которое считывается с клавиатуры (через input()).
"""


def greet_user(name):
    print(f"Привет, {name}!")

input_name = input()
greet_user(input_name)