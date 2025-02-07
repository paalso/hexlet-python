# https://ru.hexlet.io/courses/python-functions/lessons/packaging-and-unpacking-operators/exercise_unit
# https://ru.hexlet.io/code_reviews/1079182
# Python: Функции → Операторы упаковки и распаковки

# Реализовать функцию call_twice, которая должна
# - принять функцию и произвольный набор аргументов для неё,
# - вызвать функцию с заданными аргументами дважды,
# - вернуть пару из результатов вызовов (первый, затем второй).


def get_unique(*arrays):
    result = []
    for array in arrays:
        result.extend(array)
    return list(set(result))

