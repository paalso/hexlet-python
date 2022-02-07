# https://ru.hexlet.io/challenges/python_trees_converter_exercise
# https://ru.hexlet.io/code_reviews/303442

# Python: Список как словарь
# ===========================

"""
Реализуйте функцию convert(), которая принимает на вход список определённой
структуры и возвращает словарь, полученный из этого списка.

Список устроен таким образом, что с помощью него можно представлять словари.
Каждый элемент списка — тоже список из двух элементов, где первый элемент —
ключ, а второй — значение. Значение тоже может быть списком. Любой список
внутри исходного списка всегда рассматривается как данные, которые нужно
конвертировать в словарь.
"""

# Version № 1
def convert(items):
    return {key: value if type(value) != list else convert(value)
            for key, value in items}


print(convert([]))      # {}

print(convert([('key2', 'value2'), ('key', 'value')]))
# {'key2': 'value2', 'key': 'value'}

print(
    convert([
        ('key', [('key2', 'anotherValue')]),
        ('key2', 'value2')
    ])
)
# {'key': {'key2': 'anotherValue'}, 'key2': 'value2'}

# Author's version
# BEGIN
def to_item(item):
    key, value = item
    return key, convert(value) if isinstance(value, list) else value


def convert(tree):
    return dict(map(to_item, tree))
# END
