class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def set_temperature(self, temperature):

        if temperature > 30:
            result = self.temperature = temperature
            return result
        else:
            return "Температура нереальна!"


temp = Temperature(25)
print(temp.get_temperature())
print(temp.set_temperature(30))
print(temp.set_temperature(45))
print(temp.get_temperature())