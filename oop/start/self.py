class Phone:
    def __init__(self, number):
        self.number = number

    def change_number(self, number):
        self.number = number


iphone  = Phone("98977")
print(iphone.number)
iphone.change_number(1234)
print(iphone.number)

android = Phone("99988")
print(android.number)
android.change_number(999)