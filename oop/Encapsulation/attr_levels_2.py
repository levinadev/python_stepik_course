class Test:
    def __init__(self):
        self.public = "Доступно всем"
        self._protected = "Лучше не трогать"
        self.__private = "Очень скрыто"

t = Test()

# print(t.public)       # ОК
# print(t._protected)   # Работает, но плохой тон так делать
# print(t.__private)    # Ошибка: AttributeError
# ---------------

class Cat:
    def __init__(self, cat_name):
        self.name = cat_name

    def _get_host_name(self):
        return "Anna"

    __secret = "Супер секрет"


cat = Cat("Moosya")
print(cat.name)
print(cat._get_host_name())
# print(cat.__secret)

print(cat._Cat__secret)
