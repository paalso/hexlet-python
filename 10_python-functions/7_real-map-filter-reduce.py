# https://ru.hexlet.io/courses/python-functions/lessons/map-filter-reduce/exercise_unit
# https://ru.hexlet.io/code_reviews/272796

# Знакомство с map, filter, reduce
# =================================

# Реализовать функции
# - keep_truthful - должна принимать на вход итерируемый источник значений и
# возвращать итератор, отдающий только те значения из источника, которые
# "истинны" (вам пригодится функция operator.truth).

# - abs_sum - принимает на вход итерируемый источник чисел. Вернуть же
# функция должна сумму абсолютных значений этих чисел (используйте sum и abs).

# - walk - должна для некоего словаря с глубокой вложенностью уметь доставать
# значение по указанному в виде iterable строк пути. В решении можете
# использовать функцию operator.getitem.


def keep_truthful(iterable):
    return filter(bool, iterable)


def abs_sum(iterable):
    return sum(map(abs, iterable))


def walk(d, path):
    import operator, functools
    return functools.reduce(operator.getitem, path, d)


assert list(keep_truthful([True, False, "", "foo"])) == [True, 'foo']

assert abs_sum([-3, 7]) == 10
assert abs_sum([]) == 0
assert abs_sum([42]) == 42

assert walk({'a': {7: {'b': 42}}}, ["a", 7, "b"]) == 42
assert walk({'a': {7: {'b': 42}}}, ["a", 7]) == {'b': 42}