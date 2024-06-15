from unittest import main, TestCase

from src.ingredient import Ingredient, MeasurementType


class TestIngredient(TestCase):

    def setUp(self):
        self.instance = Ingredient(
            MeasurementType.GRAMS,
            "salt"
        )

    def tearDown(self):
        pass

    def test___init__(self):
        self.assertEqual(MeasurementType.GRAMS, self.instance.measurement_type)
        self.assertEqual("salt", self.instance.name)

    def test_to_json(self):
        expected_outcome = '{"name": "salt", "measurement_type": "grams"}'
        self.assertEqual(expected_outcome, self.instance.to_json())

    def test_from_json(self):
        json_string = '{"name": "salt", "measurement_type": "grams"}'
        outcome = self.instance.from_json(json_string)

        self.assertEqual(MeasurementType.GRAMS, outcome.measurement_type)
        self.assertEqual("salt", outcome.name)


if __name__ == "__main__":
    main()
