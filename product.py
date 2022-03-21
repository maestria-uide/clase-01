class Product:
    def __init__(self, title: str, value: float, currency: str):
        self.title = title
        self.value = value
        self.currency = currency

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "value": self.value,
            "currency": self.currency
        }
