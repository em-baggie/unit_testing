from src.players.human import Human


class Doctor(Human):

    def __init__(self, name, age, gender, speciality):
        super().__init__(name, age, gender)
        self.speciality = speciality

    def prescribe(self):
        pass
