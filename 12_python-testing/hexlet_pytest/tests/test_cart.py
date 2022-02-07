# https://ru.hexlet.io/courses/python-testing/lessons/bad-practice/exercise_unit
# 

# Плохие и хорошие практики тестирования
# ========================================

"""
make_cart() – создаёт новую корзину (объект).
add_item(good, count) – добавляет в корзину товары и их количество.
Товар – это объект, у которого два свойства: name (имя) и price (стоимость).
get_items() – возвращает список товаров в формате
    [{ good, count }, { good, count }, ...]
get_cost() – возвращает стоимость корзины. Стоимость корзины высчитывается
как сумма всех добавленных товаров с учётом их количества.
get_count() – возвращает общее количество товаров в корзине.

>>> cart = make_cart()
>>> cart.add_item({ 'name': 'car', 'price': 3 }, 5)
>>> cart.add_item({ 'name': 'house', 'price': 10 }, 2)
>>> len(cart.get_items())
2
>>> cart.get_cost()
35
>>> cart.add_item({ 'name': 'house', 'price': 10 }, 1)
>>> len(cart.get_items())
3
>>> cart.get_cost()
45

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
