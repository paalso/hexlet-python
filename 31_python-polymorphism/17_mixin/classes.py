class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class ShoppingCart:
    def __init__(self, items=None):
        if items is None:
            items = []
        self.items = items

    def add_item(self, item):
        self.items.append(item)
