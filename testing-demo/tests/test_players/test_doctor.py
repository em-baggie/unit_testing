from unittest import main, TestCase

from src.players.doctor import Doctor


class TestDoctor(TestCase):

    def setUp(self):
        self.instance = Doctor("dave", 30, "male", "anesthetics")

    def tearDown(self):
        pass

    def test___init__(self):
        self.assertEqual("dave", self.instance.name)
        self.assertEqual(30, self.instance.age)
        self.assertEqual("male", self.instance.gender)
        self.assertEqual("anesthetics", self.instance.speciality)

    def test_grow_older(self):
        self.instance.grow_older()
        self.assertEqual(31, self.instance.age)

        self.instance.grow_older()
        self.assertEqual(32, self.instance.age)





if __name__ == "__main__":
    main()
