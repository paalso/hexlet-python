# https://ru.hexlet.io/courses/python-declarative-programming/lessons/generator-expressions/exercise_unit

# Генераторные выражения
# =======================

# реализовать три функции. Каждая функция будет работать с
# двухмерной матрицей, то есть со списком списков (итератором итераторов):

# - each2d(test, matrix) должна проверить, что каждый элемент матрицы matrix
# удовлетворяет предикату test. Она должна вернуть False, если test вернул
# False хотя бы для одного элемента. В противном случае функция должна
# возвращать True
# - some2d(test, matrix) должна проверить, удовлетворяет ли предикату test
# хотя бы один элемент матрицы matrix. Как только test возвращает True для
# какого-либо элемента, функция должна вернуть True. Если ни один элемент
# проверку не прошел, нужно вернуть False
# - sum2d(test, matrix) должна возвращать сумму всех элементов матрицы matrix,
# удовлетворяющих предикату test


def is_int(x):
    return isinstance(x, int)


def each2d(predicate, matrix):
    return all(predicate(e) for row in matrix for e in row)


def some2d(predicate, matrix):
    return any(predicate(e) for row in matrix for e in row)


def sum2d(predicate, matrix):
    return sum(e for row in matrix for e in row if predicate(e))


assert each2d(is_int, [[1, 2], [3, 4]])
assert not each2d(is_int, [[1, None], [3, 4]])
assert each2d(is_int, [])

assert not some2d(is_int, [[None, "foo"], [(), {}]])
assert some2d(is_int, [[None, "foo"], [0, {}]])
assert not some2d(is_int, [])

assert sum2d(is_int, [[1, "Foo", 100], [False, 10, None]]) == 111
