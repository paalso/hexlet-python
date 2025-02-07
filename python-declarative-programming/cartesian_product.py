# https://ru.hexlet.io/courses/python-declarative-programming/lessons/generator-functions/exercise_unit
# https://ru.hexlet.io/code_reviews/436208

# Функции-генераторы
# ====================

# Реализовать функцию product(), которая принимает один и более позиционных
# параметров — iterable любого вида, и возвращает список кортежей.
# Возвращаемый список представляет собой декартово произведение элементов
# входных последовательностей — все сочетания "каждый с каждым"


def product(first_coll, *rest_colls):
    if len(rest_colls) == 0:
        return [(e,) for e in first_coll]

    return [(e, *items) for e in first_coll for items in product(*rest_colls)]


assert product([]) == []
assert product('q') == [('q',)]
assert product('abc') == [('a',), ('b',), ('c',)]
assert product('foo', [1, 2, 3], '') == []
assert product('A', 'B') == [('A', 'B')]
assert product([0, 1], [2, 3], [4, 5]) == [
    (0, 2, 4),
    (0, 2, 5),
    (0, 3, 4),
    (0, 3, 5),
    (1, 2, 4),
    (1, 2, 5),
    (1, 3, 4),
    (1, 3, 5),
]

# Hexlet's version
# -----------------

# BEGIN
# def product(sequence, *args):
#     subproducts = product(*args) if args else [()]
#     # ^ произведение оставшихся последовательностей вычисляем заранее
#     # чтобы не строить заново для каждого элемента первой последовательности
#     return [
#         (first,) + subproduct
#         for first in sequence
#         for subproduct in subproducts
#     ]
# END