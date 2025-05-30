class Mouse:
    def __return_hello(self):
        return "Hello"

    def get_hello_method(self):
        return self.__return_hello()


mouse = Mouse()
print(mouse.get_hello_method())
