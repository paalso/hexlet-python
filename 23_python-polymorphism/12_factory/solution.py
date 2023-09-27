#!/usr/bin/env python3

# https://ru.hexlet.io/courses/python-polymorphism/lessons/factory/exercise_unit
# https://ru.hexlet.io/code_reviews/1160077

# Python: Полиморфизм
# 12. Фабрика(Паттерн)

import pathlib
from config_factory import ConfigFactory


def main():
    filepath = pathlib.Path.cwd().joinpath('tests/fixtures', 'test.yml')
    config = ConfigFactory.factory(filepath)
    print(config)

    filepath = pathlib.Path.cwd().joinpath('tests/fixtures', 'test2.json')
    config = ConfigFactory.factory(filepath)
    print(config)
    print(config.get_value('key'))  # value


if __name__ == '__main__':
    main()
