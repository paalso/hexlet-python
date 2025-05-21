import os

from config_klass import Config
from parsers.json_parser import JSONParser
from parsers.yaml_parser import YAMLParser

PARSERS = {
    ".yaml": YAMLParser,
    ".yml": YAMLParser,
    ".json": JSONParser,
}


class ConfigFactory:
    @classmethod
    def factory(cls, path):
        ext = cls.get_extention(path)
        parser = PARSERS.get(ext)
        return Config(parser.parse(path))

    @staticmethod
    def get_extention(path):
        return os.path.splitext(path)[-1]
