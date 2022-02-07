# https://ru.hexlet.io/courses/python-functions/lessons/map-filter-reduce/exercise_unit
# Знакомство с map, filter, reduce

# Реализуйте функцию filter_map, которая ведёт себя подобно filter и map,
# работающим вместе. filter_map должна принимать в качестве аргументов функцию и
# итерируемый источник, а возвращать должна список.
#
# В теле filter_map к каждому значению из источника нужно применять функцию,
# которая в ответ будет возвращать пару:
# - Булево значение,
# - Некий результат.
# Если булево значение (1) истинно, то результат (2) должен попадать в
# результирующий список. В противном случае второе значение пары игнорируется.


def filter_map(func, coll):
    result = []
    for item in coll:
        predicat, value = func(item)
        if predicat:
            result.append(value)
    return result


def make_stars(x):
    if x > 0:
        return True, '*' * x
    return False, ''


for s in filter_map(make_stars, [1, 0, 5, -5, 2]):
    print(s)