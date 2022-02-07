# https://ru.hexlet.io/courses/python-trees/lessons/definition/exercise_unit
# https://ru.hexlet.io/code_reviews/303438

# Определения
# ============
"""
В этом задании под деревом понимается любой список элементов, которые в свою
очередь могут быть также деревьями (списками).
Реализуйте функцию, которая принимает на вход дерево, и возвращает новое,
элементами которого являются дети вложенных узлов.
"""

import itertools


def remove_first_level(tree):
    return list(itertools.chain(*filter(lambda e: type(e) == list, tree)))


tree1 = [[5], 1, [3, 4]]
assert remove_first_level(tree1) == [5, 3, 4]
tree2 = [1, 2, [3, 5], [[4, 3], 2]]
assert  remove_first_level(tree2) == [3, 5, [4, 3], 2]
