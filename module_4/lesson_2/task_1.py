"""
Создайте класс User, который:
В конструкторе принимает имя (name) и возраст (age).
Имеет метод info(), который выводит на экран строку в формате: "Имя: {name}, Возраст: {age}".
Создайте объект User("Анна", 25) и вызовите метод info().
"""

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")


user = User("Анна", 25)
user.info()