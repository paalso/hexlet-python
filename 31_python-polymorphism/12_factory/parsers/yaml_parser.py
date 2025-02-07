import yaml


class YAMLParser():
    def __init__(self, path):
        with open(path, 'r') as fp:
            self.data = yaml.safe_load(fp)

    def get_data(self):
        return self.data
