# уровни доступа к атрибутам:
# 1. Одиночное подчеркивание _
# 2. Двойное подчеркивание __
#
#
# пример 1 с одиночным подчеркиванием


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def host_name(self):
        host_name = "Anna"


cat = Cat("Barsik", 4)
print(cat.name)
print(cat.age)

print(cat.host_name)

# пример 2 с двойным подчеркиванием