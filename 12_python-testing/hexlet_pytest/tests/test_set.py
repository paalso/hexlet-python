# https://ru.hexlet.io/courses/python-testing/lessons/fixtures/exercise_unit
# https://ru.hexlet.io/code_reviews/473695

# Подготовка данных
# ================

"""
Напишите тесты для функции set(coll, path, value) возвращающей словарь,
в котором она изменяет (или добавляет) значение по указанному пути.
Функция мутирует словарь:

>>> coll = { "a": { "b": { "c": 3 } } }
>>> set(coll, ["a", "b", "c"], 4)
>>> coll["a"]["b"]["c"]
4

>>> set(coll, ['x', 'y', 'z'], 5)
>>> coll['x']['y']['z']
5
"""


import pytest
from hexlet_pytest.set_functions import get_function

set_ = get_function("right")
set_ = get_function("wrong1")
set_ = get_function("wrong3")
set_ = get_function("wrong2")


@pytest.fixture
def get_coll():
    return { "a": { "b": { "c": 3 } } }


def test_set_(get_coll):
    coll = get_coll
    # print(coll)

    set_(coll, ["a", "b", "c"], 4)
    # print(coll)
    assert coll == {'a': {'b': {'c': 4}}}

    set_(coll, ["a", "b", "c", "d"], 5)
    assert coll == {'a': {'b': {'c': {'d': 5}}}}

    set_(coll, ["a", "b", "c", "e"], 6)
    assert coll == {'a': {'b': {'c': {'d': 5, 'e': 6}}}}

    set_(coll, ["a", "b"], 4)
    assert coll == {'a': {'b': 4}}

    set_(coll, ["x", "y", "z"], 5)
    assert coll == {'a': {'b': 4}, 'x': {'y': {'z': 5}}}


# Author's version
"""
def test_plain_set():
    # TODO: use parametrizing tests
    data = {"a": {"b": {"c": "d"}}}
    data_copy = copy.deepcopy(data)
    set_(data, ['a'], 'value')

    data_copy['a'] = 'value'
    assert data_copy == data


def test_nested_set():
    data = {"a": {"b": {"c": "d"}}}
    data_copy = copy.deepcopy(data)
    set_(data, ['a', 'b', 'c'], 'value')
    data_copy['a']['b']['c'] = 'value'
    assert data_copy == data


def test_new_property_set():
    data = {"a": {"b": {"c": "d"}}}
    data_copy = copy.deepcopy(data)
    set_(data, ['a', 'b', 'd'], 'value')
    data_copy['a']['b']['d'] = 'value'
    assert data_copy == data
"""
