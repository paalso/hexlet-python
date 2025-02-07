# https://ru.hexlet.io/courses/python-testing/lessons/pytest/exercise_unit

# Pytest
# =======

"""
Напишите тесты для функции without(coll, *values), которая принимает первым
параметром список и возвращает его копию, из которой исключены значения,
переданные вторым и последующими параметрами.
"""


assert take([], 0) == []
assert take([], 1) == []
assert take([]) == []

L = [1,2,3,4,5]
assert take(L, 0) == []
assert take(L, 1) == [1]
assert take(L, 3) == [1,2,3]
assert take(L, len(L)) == L
assert take(L, len(L) + 3) == L
assert take(L) == [1]