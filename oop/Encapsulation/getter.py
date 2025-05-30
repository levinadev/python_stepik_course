# примеры использования геттеров
#

class Cat:
    def __init__(self, name):
        self.__name = name  # приватный атрибут

    def get_name(self):
        return self.__name  # геттер: аккуратно отдаём имя


cat = Cat("Муся")
print(cat.get_name())  # → Муся


# ---

class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self.__age



some_person = Person("Alex", 29)
print(some_person.get_name()) # правильно
print(some_person.get_age())  # правильно и работает

print(some_person._name) # не правильно
print(some_person.__age) # не правильно и выдаст ошибку вообще


