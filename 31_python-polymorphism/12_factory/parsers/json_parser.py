import json


class JSONParser():
    def __init__(self, path):
        with open(path, 'r') as fp:
            self.data = json.load(fp)

    def get_data(self):
        return self.data
