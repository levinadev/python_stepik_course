"""
Создайте класс User с:
Конструктором, принимающим имя и возраст.
Методом have_birthday(), который увеличивает возраст на 1.
Создайте объект User("Мария", 20), вызовите метод have_birthday() два раза и выведите возраст.
"""


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def have_birthday(self):
        self.age += 1


user = User("Мария", 20)
user.have_birthday()
user.have_birthday()

print(user.age)