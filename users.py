class Users:
    def __init__(self, name: str, username: str, email: str):
        self.name = name
        self.username = username
        self.email = email

    def to_dictr(self) -> dict:
        return {
            "name": self.name,
            "email": self.username,
            "email": self.email
        }
