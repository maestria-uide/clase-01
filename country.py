class Country:
    def __init__(self, name: str):
        self.name = name


    def to_dictr(self) -> dict:
        return {
            "name": self.name,

        }
