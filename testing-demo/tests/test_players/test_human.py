from unittest import main, TestCase
from unittest.mock import patch

from src.players.human import Human


class TestHuman(TestCase):

    def setUp(self):
        self.instance = Human("dave", 30, "male")

    def tearDown(self):
        pass

    def test___init__(self):
        self.assertEqual("dave", self.instance.name)
        self.assertEqual(30, self.instance.age)
        self.assertEqual("male", self.instance.gender)

    def test_grow_older(self):
        self.instance.grow_older()
        self.assertEqual(31, self.instance.age)
        self.instance.grow_older()
        self.assertEqual(33, self.instance.age)

    @patch("src.players.human.print")
    def test_say_hi(self, mock_print):
        self.instance.say_hi()
        self.assertEqual(
            1,
            len(mock_print.call_args_list)
        )
        print(self.instance)


if __name__ == "__main__":
    main()
