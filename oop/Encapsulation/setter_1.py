class Person:
    def __init__(self, age):
        self.__age = age

    def set_age(self, new_age):
        if new_age >= 0:
            self.__age = new_age
        else:
            print("Возраст не может быть отрицательным!")

    def get_age(self):
        return self.__age


p = Person(30)
p.set_age(25)       # всё ок
print(p.get_age())  # → 25

p.set_age(-5)       # ❌ не даст установить
print(p.get_age())  # → 25 (не изменилось!)
