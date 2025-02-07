class Config:
    def __init__(self, data=None):
        if data is None:
            data = {}
        self.data = data

    def __str__(self):
        return str(self.data)

    def get_value(self, key):
        result = self.data[key]
        if isinstance(result, dict):
            return Config(result)
        return result
