#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# https://ru.hexlet.io/courses/python-testing/lessons/tdd/exercise_unit
# https://ru.hexlet.io/code_reviews/477292

# Разработка через тестирование (TDD)
# ====================================


import pytest
from hexlet_pytest.fill import fill


@pytest.fixture(name='collection')
def get_collection():
    return [1, 2, 3, 4]


def test_fill_with_given_limits(collection):
    fill(collection, '*', 1, 1)
    assert collection == [1, 2, 3, 4]

    fill(collection, '*', 1, 0)
    assert collection == [1, 2, 3, 4]

    fill(collection, '*', 0, -1)
    assert collection == ['*', '*', '*', 4]

    fill(collection, '%', 0, -5)
    assert collection == ['*', '*', '*', 4]

    fill(collection, '&', 1, 3)
    assert collection == ['*', '&', '&', 4]

    fill(collection, '#', 2, 10)
    assert collection == ['*', '&', '#', '#']

    fill(collection, '+', -2, 3)
    assert collection == ['*', '&', '+', '#']


def test_fill_without_given_limits(collection):
    fill(collection, '*')
    assert collection == ['*', '*', '*', '*']


def test_fill_without_end_limit(collection):
    fill(collection, '*', 4)
    assert collection == [1, 2, 3, 4]

    fill(collection, '*', 2)
    assert collection == [1, 2, '*', '*']

    fill(collection, '+', -2)
    assert collection == [1, 2, '+', '+']

    fill(collection, '~', -5)
    assert collection == ['~', '~', '~', '~']

