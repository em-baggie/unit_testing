

class Human:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def grow_older(self):
        if self.age == 31:
            self.age += 1
        self.age += 1

    def say_hi(self):
        print("hey my name is ", self.name)
