# https://ru.hexlet.io/courses/python-trees/lessons/calculate/theory_unit/exercise_unit
# https://ru.hexlet.io/code_reviews/353038

# Аггрегация 2
# =============
"""
Реализуйте функцию du, которая принимает на вход директорию, а возвращает
список узлов, вложенных (директорий и файлов) в указанную директорию на один
уровень, и место, которое они занимают. Размер файла задается в метаданных.
Размер директории складывается из сумм всех размеров файлов, находящихся внутри
во всех подпапках. Сами папки размера не имеют.
"""

import fs
from fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


def total_space(node):
    if is_file(node):
        return get_meta(node).get('size', 0)
    return sum(map(total_space, get_children(node)))


def du(node):
    return sorted(map(
        lambda node: (get_name(node), total_space(node)),
        get_children(node)),
            key=lambda pair:-pair[1])


tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])



print(du(tree))     # [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]
assert du(tree) == [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]

print(du(get_children(tree)[0]))     # [('etc', 10280), ('hosts', 3500), ('resolve', 1000)]
expected = [('consul', 9480), ('nginx', 800), ('apache', 0)]
assert du(get_children(tree)[0]) == expected