from parsers.json_parser import JSONParser
from parsers.yaml_parser import YAMLParser
from config_klass import Config


PARSERS = {
    '.yaml': YAMLParser,
    '.yml': YAMLParser,
    '.json': JSONParser,
}


class ConfigFactory:
    def factory(filepath):
        filepath_extension = filepath.suffix
        parser = PARSERS[filepath_extension]
        return Config(parser(filepath).get_data())
