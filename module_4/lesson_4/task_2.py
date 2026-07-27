"""
Создайте класс Animal с:

Методом speak(), который выводит "Животное издаёт звук".
Создайте класс Cat, который наследует от Animal и переопределяет метод speak() так, чтобы он выводил "Мяу!".
Создайте объект Cat() и вызовите метод speak().
"""

class Animal:
    def speak(self):
        print("Животное издаёт звук")

class Cat(Animal):
    def speak(self):
        print("Мяу!")

cat = Cat()
cat.speak()