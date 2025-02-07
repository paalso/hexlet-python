# https://ru.hexlet.io/courses/python-functions/lessons/more-keyword-arguments/exercise_unit

# Больше об именованных аргументах
# ===================================

# Реализовать функцию updated. Эта функция должна принимать словарь в
# качестве единственного позиционного аргумента (обязательного) и произвольное
# кол-во именованных аргументов. Возвращать же функция должна новую версию
# словаря, в котором ключи, соответствующие именованным аргументам, должны
# иметь сопутствующие значения


def updated(d, **kwargs):
    d_copy = d.copy()
    d_copy.update(kwargs)
    return d_copy


d = {'a': 1, 'b': False}
assert updated(d, a=2, b=True, c=None) == {'a': 2, 'b': True, 'c': None}
assert d == {'a': 1, 'b': False}
assert updated(d) == d
assert not updated(d) is d
