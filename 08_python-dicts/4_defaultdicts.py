# https://ru.hexlet.io/courses/python-dicts/lessons/defaultdicts/exercise_unit


# Python: Словари и Множества → Инициализация новых значений и defaultdicts

# Реализовать функцию collect_indexes. Эта функция должна принимать на вход
# коллекцию (некий iterator/iterable) и возвращать словарь (или подобная ему
# коллекция!), где ключом будет элемент коллекции, а значением для ключа —
# список индексов коллекции, по которым встречается этот элемент.


def collect_indexes(items):
    import collections
    d = collections.defaultdict(list)
    [d[e].append(i) for i, e in enumerate(items)]
    return d


d = collect_indexes("hello")
print(d)
