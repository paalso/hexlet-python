# https://ru.hexlet.io/courses/python-dicts/lessons/sets/exercise_unit
# Python: Словари и Множества → Множества

# Реализовать функцию all_unique, которая должна принимать итератор (в т.ч. и
# те, которые не перезапускаемые!) и возвращать True, если элементы в итераторе
# не повторяются (если элементов нет, то ничего не повторяется!).


def all_unique(items):
    L = list(items)
    return len(L) == len(set(L))


assert all_unique([])
assert all_unique("cat")
assert all_unique([1, 2, 3])
assert not all_unique([1, 2, 1])
assert all_unique(iter([1]))


"""
def all_unique(iterable):
    items = list(iterable)
    return len(items) == len(set(items))
"""
