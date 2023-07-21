#!/usr/bin/env python3

# https://ru.hexlet.io/courses/python-dicts/lessons/hash-table/exercise_unit
# https://ru.hexlet.io/code_reviews/1088418


# Python: Словари и Множества → Хеш-таблицы
# Реализуйте функцию get_or_default(). Она должна возвращать из хеш-таблицы
# значение по ключу или значение по умолчанию, если такой записи не существует.

from map import get_hash, make_map


def get_or_default(map_, key, default_value):
    hash = get_hash(key)
    map_value = map_[hash]
    return map_value[1] if map_value else default_value


m = make_map()

# метод set(ключ, значение) записывает значение по ключу в мапу
m.set("g", "bar")
m.set("e", "foo")
m.set("b", "boo")
print(m)

print(get_or_default(m, "g", "python")) # bar
print(get_or_default(m, "a", "python")) # python
