"""
Создайте класс Book с:
Публичным атрибутом title (название).
Приватным атрибутом __author (автор).
Конструктором, принимающим оба значения.
Геттером для __author.

Создайте объект Book("Война и мир", "Толстой").
Выведите название и автора через геттер.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author

    @property
    def author(self):
        return self.__author



book = Book("Война и мир", "Толстой")
print(book.title)
print(book.author)