"""
Создайте класс Person с:
Конструктором, принимающим имя (name).
Методом introduce(), который выводит: "Меня зовут {name}".
Создайте класс Student, который наследует от Person и ничего не переопределяет.

Создайте объект Student("Анна") и вызовите метод introduce().
"""

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Меня зовут {self.name}")

class Student(Person):
    pass

student = Student("Анна")
student.introduce()