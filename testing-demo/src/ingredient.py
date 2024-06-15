import json
from enum import Enum


class MeasurementType(Enum):
    KG = "kg"
    GRAMS = "grams"


class Ingredient:

    def __init__(self, measurement_type: MeasurementType, name: str):
        self.measurement_type = measurement_type
        self.name = name

    def to_json(self):
        payload = {
            "name": self.name,
            "measurement_type": self.measurement_type.value
        }
        return json.dumps(payload)

    def from_json(self, json_str):
        json_dict = json.loads(json_str)
        measurement_type = MeasurementType(
            json_dict["measurement_type"]
        )
        return Ingredient(
            measurement_type,
            json_dict["name"]
        )