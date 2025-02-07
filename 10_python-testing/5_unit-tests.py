# https://ru.hexlet.io/courses/python-testing/lessons/unit-tests/exercise_unit
# https://ru.hexlet.io/code_reviews/470628

# Модульные тесты
# ================

"""
Напишите тесты для валидатора, который проверяет корректность данных.
Принцип работы валидатора следующий:

С помощью метода add_check(fn) в него добавляются проверки. Каждая проверка
представляет из себя функцию-предикат, которая принимает на вход проверяемое
значение и возвращает либо True либо False в зависимости от того, соответствует
ли значение требованиям проверки или нет.
С помощью метода is_valid(value), пользователь проверяет соответствие значения
всем добавленным проверкам. Если не было добавлено ни одной проверки,
считается, что любое значение верное.
"""


def test_validator():
    add_check, is_valid = make_validator()
    assert is_valid("value")
# BEGIN (write your solution here)

    # проверка на положительный целый квадрат
    add_check(lambda x: x > 0)
    add_check(lambda x: (x ** 0.5) ** 2 == x)

    assert is_valid(25)
    assert is_valid(81)


def test_validator_false():
    add_check, is_valid = make_validator()

    # проверка на положительное нечетное число
    add_check(lambda x: x > 0)
    add_check(lambda x: x % 2 == 1)

    assert not is_valid(20)
    assert not is_valid(-1)

# END

