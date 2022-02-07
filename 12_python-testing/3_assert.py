# https://ru.hexlet.io/courses/python-testing/lessons/assert/exercise_unit

# Утверждения (Asserts)
# ======================

"""
Напишите тесты для функции take(items, n), которая возвращает
первые n элементов из списка:
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