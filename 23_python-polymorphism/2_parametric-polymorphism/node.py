class Node:
    def __init__(self, value, node=None):
        self.next = node
        self.value = value

    def get_next(self):
        return self.next

    def get_value(self):
        return self.value

    def __repr__(self):
        acc = []
        current = self
        while current is not None:
            acc.append(current.get_value())
            current = current.get_next()
        return str(tuple(acc))
