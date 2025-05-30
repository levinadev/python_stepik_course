class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # Доступ к атрибуту открыт

account = BankAccount(1000)
account.balance = -500  # Мы случайно (или намеренно) сделали баланс отрицательным
# print(account.balance)  # -500

class Person:
    def __init__(self, name):
        self._name = name  # защищённый атрибут

    @property
    def name(self):  # геттер
        print("Чтение имени")
        return self._name

    @name.setter
    def name(self, value):  # сеттер
        print("Установка имени")
        if not value:
            raise ValueError("Имя не может быть пустым")
        self._name = value

p = Person("Аня")
print(p.name)    # → Чтение имени → Аня
p.name = "Катя"  # → Установка имени
