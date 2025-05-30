class Dog:
    def __init__(self, name):
        self._name = name          # защищённый атрибут
        self.__mood = "happy"      # приватный атрибут

    def _get_name_upper(self):
        # защищённый метод — возвращает имя заглавными
        return self._name.upper()

    def get_name(self):
        # геттер, который обращается к защищённому методу
        return self._get_name_upper()


dog = Dog("Groovy")
print(dog.get_name())  # → BOBBY

# А так напрямую к этим методам обращаться не стоит (хотя технически можно):
print(dog._get_name_upper())  # можно, но не рекомендуется
# print(dog.__get_mood())     # Ошибка! Нет такого метода (приватный скрыт)
