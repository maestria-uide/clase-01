class Ingredients:
    def __init__(self, strCategory: str):
        self.strCategory = strCategory


    def to_dictr(self) -> dict:
        return {
            "strCategory": self.strCategory,

        }