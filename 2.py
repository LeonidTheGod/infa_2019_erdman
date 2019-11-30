class Dog:
    def __init__(self, angry, count):
        self.angry = angry
        self.count = count
    def __str__(self):
        return self.angry + ' ' + str(self.angry)

    def say_gaw(self):
        if self.angry:
            print('GAW-' * self.count)
        else:
            print('gaw-' * self.count)

my_dog = Dog(True, 3)
my_dog.say_gaw()   
my_dog.__str__()

