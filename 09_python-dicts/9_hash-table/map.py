class Map(list):
    def __setitem__(self, index, value):
        try:
            super().__setitem__(index, value)
        except IndexError:
            for _ in range(index - len(self) + 1):
                self.append(None)
            super().__setitem__(index, value)

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return None

    def set(self, key, value):
        index = get_hash(key)
        self[index] = (key, value)


def make_map():
    return Map()


def get_hash(key):
    return sum(ord(ch) for ch in key) % 10 + 1
