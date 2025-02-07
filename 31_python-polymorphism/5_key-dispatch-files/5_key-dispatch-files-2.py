# https://ru.hexlet.io/courses/python-polymorphism/lessons/key-dispatch-files/exercise_unit
# https://ru.hexlet.io/code_reviews/1143490

# Python: Полиморфизм
# 5. Диспетчеризация по имени файла

'''
Реализуйте класс DatabaseConfigLoader, который отвечает за загрузку
конфигурации для базы данных. У класса следующий интерфейс:

__init__() - принимает на вход путь, по которому искать конфигурацию
load(env) - метод, который грузит конфигурацию для конкретной среды окружения.
Он загружает файл database.{env}.json, парсит его и возвращает результат наружу.
'''


import json
from pathlib import Path


class DatabaseConfigLoader:
    def __init__(self, path_to_configs) -> None:
        self.path_to_configs = Path(path_to_configs)

    def load(self, env):
        config = self.__get_env_config(env)
        if 'extend' not in config:
            return config
        extended_cofig = self.load(config['extend']) | config
        extended_cofig.pop('extend')
        return extended_cofig

    def __get_env_config(self, env):
        file_name = f'database.{env}.json'
        file_path = self.path_to_configs / file_name
        with open(file_path, 'r') as fd:
            config = json.load(fd)
        return config


db_cfg_loader = DatabaseConfigLoader('fixtures')

# print(db_cfg_loader.load('custom')) 
# print(db_cfg_loader.load('development'))
# print(db_cfg_loader.load('preproduction'))
# print(db_cfg_loader.load('production'))

print(db_cfg_loader.load('preproduction'))
