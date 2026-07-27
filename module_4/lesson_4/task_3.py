"""
Создайте класс Animal с:
Конструктором, принимающим имя (name).
Создайте класс Dog, который наследует от Animal и:
В конструкторе принимает имя (name) и породу (breed).
Вызывает конструктор родителя через super().__init__(name).
Сохраняет породу в атрибут self.breed.

Создайте объект Dog("Бобик", "Овчарка") и выведите имя и породу через пробел.
"""

class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

dev = Developer("Евгений", "Python")
print(dev.name, dev.language)