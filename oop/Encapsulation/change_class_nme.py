class Person:
    def __init__(self, name):
        self.name = name


person = Person("John")
print(person.name)

person.name = "Anna"
print(person.name)

person.name = "Sonya"
print(person.name)