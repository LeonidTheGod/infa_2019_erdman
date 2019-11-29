class Dog:
    def __init__(self, angry, count):
        self.angry = angry
        self.count = count

    def say_gaw(self):
        if self.angry:
            print('GAW-' * self.count)
        else:
            print('gaw-' * self.count)

my_dog = Dog(True, 3)
my_dog.say_gaw()      # ошибки нет, напечатает Gaw-gaw
