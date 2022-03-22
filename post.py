class Post:
    def __init__(self, title: str, body:str):
        self.title = title
        self.body = body


    def to_dictr(self) -> dict:
        return {
            "title": self.title,
            "body": self.body

        }