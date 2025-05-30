class Account:
    def __init__(self, balance, name, age, city, country):
        self.balance = balance
        self.name = name
        self.age = age
        self.city = city
        self.country = country


account_anya = Account("1k", "Anya", 29,"SPb", "Russia")
print(account_anya.balance)
print(account_anya.name)
print(account_anya.age)
print(account_anya.city)
print(account_anya.country)
print(account_anya)

