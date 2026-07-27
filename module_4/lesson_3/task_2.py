"""
Создайте класс User с приватным атрибутом __name. Конструктор принимает имя.
Добавьте геттер @property для доступа к имени.
Создайте объект User("Анна") и выведите имя через геттер.
"""

class User:
    def __init__(self, name):
        self.__name = name

    @property
    def get_name(self):
        return self.__name


user = User("Анна")
print(user.get_name)

