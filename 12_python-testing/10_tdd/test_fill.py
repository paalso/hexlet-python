#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# https://ru.hexlet.io/courses/python-testing/lessons/tdd/exercise_unit
# https://ru.hexlet.io/code_reviews/477292

# Разработка через тестирование (TDD)
# ====================================


'''
coll =  [1, 2, 3, 4]
 
fill(coll, '*', 1, 3)
print(coll)  # => [1, '*', '*', 4]
 
fill(coll, '*')
print(coll)  # => ['*', '*', '*', '*']
 
fill(coll, '*', 4)
print(coll)  # => [1, 2, 3, 4]
 
fill(coll, '*', 0, 10)
print(coll)  # => ['*', '*', '*', '*']
'''
import pytest
from solution import fill


@pytest.fixture(name='collection')
def _collection():
    return [1, 2, 3, 4]


def test_fill(collection):
    fill(collection, '*', 1, 3)
    assert collection == [1, '*', '*', 4]


# BEGIN (write your solution here)
def test_empty_coll():
    collection = []

    fill(collection, '*', 1, 3)
    assert collection == []


def test_nonempty_coll1(collection):

    fill(collection, '*', 1, 3)
    assert collection == [1, '*', '*', 4]

    fill(collection, '*')
    assert collection == ['*', '*', '*', '*']


def test_nonempty_coll2(collection):

    fill(collection, '*', 4)
    assert collection == [1, 2, 3, 4]
    
    fill(collection, '*', 0, 10)
    assert collection == ['*', '*', '*', '*']

    fill(collection, '#', -1, 10)
    assert collection == ['#', '#', '#', '#']

    fill(collection, '%', 10, -1)
    assert collection == ['#', '#', '#', '#']

    fill(collection, '$', 2, 3)
    assert collection == ['#', '#', '$', '#']
 
# END
