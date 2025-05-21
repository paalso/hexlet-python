import json


class JSONParser:
    @staticmethod
    def parse(path):
        with open(path, 'r') as f:
            return json.loads(f.read())
