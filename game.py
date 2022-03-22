class Game:
    def __init__(self, title: str):
        self.title = title


    def to_dictr(self) -> dict:
        return {
            "title": self.title,

        }