class Rates:
    def __init__(self, name: str, unit: str, value: str):
        self.name = name
        self.unit = unit
        self.value = value

    def to_dictr(self) -> dict:
        return {
            "name": self.name, "unit": self.unit, "value": self.value

        }
