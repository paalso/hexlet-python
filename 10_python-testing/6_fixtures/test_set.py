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
from set_functions import get_function

set_ = get_function("wrong2")
set_ = get_function("wrong3")
set_ = get_function("wrong1")

set_ = get_function("right")


@pytest.fixture
def coll():
    return {'a': {'b': {'c': 3}}}


def test_existing_path_update(coll):
    set_(coll, ['a', 'b', 'c'], 4)
    assert coll == {'a': {'b': {'c': 4}}}


def test_inc_path_nesting(coll):
    set_(coll, ['a', 'b', 'c', 'd'], 5)
    assert coll == {'a': {'b': {'c': {'d': 5}}}}


def test_dec_path_nesting(coll):
    set_(coll, ['a'], 5)
    assert coll == {'a': 5}


def test_existing_path_update_with_new_key(coll):
    set_(coll, ['a', 'b', 'd'], 7)
    assert coll == {'a': {'b': {'c': 3, 'd': 7}}}


def test_new_path_set(coll):
    set_(coll, ['x', 'y', 'z'], 5)
    assert coll == {'a': {'b': {'c': 3}}, 'x': {'y': {'z': 5}}}


def test_to_empty_dict_set():
    coll = {}
    set_(coll, ['x', 'y', 'z'], 5)
    assert coll == {'x': {'y': {'z': 5}}}


# Author's version
"""
@pytest.fixture
def data():
    return {"a": {"b": {"c": "d"}}}


def test_plain_set(data):
    data_copy = copy.deepcopy(data)
    set_(data, ['a'], 'value')
    data_copy['a'] = 'value'
    assert data_copy == data


def test_nested_set(data):
    data_copy = copy.deepcopy(data)
    set_(data, ['a', 'b', 'c'], 'value')
    data_copy['a']['b']['c'] = 'value'
    assert data_copy == data


def test_new_property_set(data):
    data_copy = copy.deepcopy(data)
    set_(data, ['a', 'b', 'd'], 'value')
    data_copy['a']['b']['d'] = 'value'
    assert data_copy == data
"""
