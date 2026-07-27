"""
Создайте класс User с:
Конструктором, принимающим имя.
Методом change_name(new_name), который изменяет имя пользователя.
Создайте объект с именем "Анна", измените имя на "Анна Иванова" и выведите новое имя.
"""


class User:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name


user = User("Анна")
user.change_name("Анна Иванова")
print(user.name)