class BadUser:
    def __init__(self, name):
        self.name = name
        self._age = 0
        self.__password = "12345"

    def get_name(self):
        print(self.name)

    def get_age(self):
        print(self._age)

    def get_password(self):
        print(self.__password)

# создаём пользователя
user = BadUser("Masha")

# вызываем геттеры
user.get_name()       # → просто print, не возвращает данные
user.get_age()        # → просто print
user.get_password()   # → выдает приватный пароль 😱

print("----")

class GoodUser:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.__password = "12345"

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    # не даём доступ к паролю!
    def check_password(self, password):
        return password == self.__password


user = GoodUser("Masha", 25)

print(user.get_name())          # → Masha
print(user.get_age())           # → 25
print(user.check_password("12345"))  # → True (а сам пароль мы не отдали!)
