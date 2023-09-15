import copy


class InMemoryKV:
    def __init__(self, dict_: dict) -> None:
        self.storage = copy.deepcopy(dict_)

    def get_(self, key, default=None):
        return self.storage.get(key, default)

    def set_(self, key, value):
        self.storage[key] = value

    def unset_(self, key):
        self.storage.pop(key, None)

    def clear_(self):
        return self.storage.clear()

    def to_dict(self):
        return copy.deepcopy(self.storage)
