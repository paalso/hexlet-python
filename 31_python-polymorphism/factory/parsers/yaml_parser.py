import yaml


class YAMLParser:
    @staticmethod
    def parse(path):
        with open(path, 'r') as f:
            return yaml.safe_load(f.read())
