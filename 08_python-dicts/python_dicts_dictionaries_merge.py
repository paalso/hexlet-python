# https://ru.hexlet.io/challenges/python_dicts_scrabble
# https://ru.hexlet.io/code_reviews/248510

# Python: Слияние словарей
# =========================

# Реализуйте функцию merged, которая объединяет несколько словарей в один
# общий словарь. Функция принимает любое количество аргументов и возвращает
# результат в виде словаря, в котором каждый ключ содержит множество (set)
# уникальных значений.


def merged(*dicts):
    import collections
    result = collections.defaultdict(set)
    for d in dicts:
        for key, value in d.items():
            result[key].add(value)
    return dict(result)


d1 = {'a': 1, 'b': 2}
d2 = {'b': 10, 'c': 100}

print(merged(d1, d2))
