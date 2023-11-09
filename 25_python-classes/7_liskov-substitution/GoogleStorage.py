class GoogleStorage:
    def __init__(self):
        self.elements = {}

    def get(self, key):
        return self.elements.get(key)

    def set(self, key, value):
        self.elements[key] = value

    def count(self):
        raise Exception
