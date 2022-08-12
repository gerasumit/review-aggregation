from tokenize import String


class ProductDetail:
    description: str
    model: str

    def __init__(self, description: str, model: str = None):
        self.description = description
        self.model = model