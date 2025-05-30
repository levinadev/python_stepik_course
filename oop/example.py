
def feed(animail_type):
    if animail_type == 'Cat':
        print("Meow")
    if animail_type == 'Dog':
        print("Bow")


# feed('Cat')
# feed('Dog')


class Animail:
    def __init__(self, animail_type):
        self.animail_type = animail_type



Animail_1 = Animail('Cat')
print(Animail_1.animail_type)

Animail_2 = Animail('Dog')
print(Animail_2.animail_type)



