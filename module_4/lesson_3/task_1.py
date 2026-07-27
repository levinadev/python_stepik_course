"""
Создайте класс User с приватным атрибутом __password. Конструктор принимает пароль и сохраняет его в приватный атрибут.
Создайте объект User("12345") и попытайтесь вывести user.__password.
"""

class User:
    def __init__(self, password):
        self.__password = password

user = User("12345")
try:
    print(user.__password)
except AttributeError:
    print("Ошибка: 'User' object has no attribute '__password'")