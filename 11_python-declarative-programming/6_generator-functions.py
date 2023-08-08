# https://ru.hexlet.io/courses/python-declarative-programming/lessons/generator-functions/exercise_unit

# Функции-генераторы
# ====================

# написать
# Функцию my_map(f, xs), которая должна работать как упрощенная версия map()
# Функцию my_filter(f, xs) — упрощенный вариант filter()
# Функцию replicate_each(n, xs) должен выдавать на выход по n копий для
# каждого элемента итератора xs


def my_map(func, items):
    for e in items:
        yield func(e)


def my_filter(func, items):
    for e in items:
        if func(e):
            yield e


def replicate_each(times, items):
    for e in items:
        for _ in range(times):
            yield e


assert list(my_map(abs, [-1, 2, -3])) == [1, 2, 3]
assert list(my_filter(lambda x: x % 2 == 1, range(10))) == [1, 3, 5, 7, 9]
assert list(replicate_each(1, [1, 'a'])) == [1, 'a']
assert list(replicate_each(3, [1, 'a'])) == [1, 1, 1, 'a', 'a', 'a']
assert list(replicate_each(0, [1, 'a'])) == []


"""
def replicate_each(number, source):
    for value in source:
        yield from (value for _ in range(number))
        # "yield from i", это сокращенная форма для
        #
        # for x in i:
        #     yield x
"""
