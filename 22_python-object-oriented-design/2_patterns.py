# https://ru.hexlet.io/courses/python-object-oriented-design/lessons/patterns/exercise_unit
# https://ru.hexlet.io/code_reviews/1131296

# Python: Объектно-ориентированный дизайн 
# 2. Шаблоны Проектирования

# Реализуйте функцию to_Klass(), которая принимает на вход cловарь и возвращает
# объект типа Klass такой же структуры.

from dataclasses import dataclass


@dataclass
class Klass:
    pass


def to_Klass(dict_):
    klass = Klass()
    for key, value in dict_.items():
        setattr(klass, key, value)
    return klass


data = {
    'key': 'value',
    'key2': 'value2',
}

config = to_Klass(data)

assert config.key == 'value'
assert config.key2 == 'value2'
