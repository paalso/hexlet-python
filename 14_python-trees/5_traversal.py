# https://ru.hexlet.io/courses/python-trees/lessons/traversal/
# https://ru.hexlet.io/code_reviews/351944

# Обход дерева
# ============================================
"""
Реализуйте функцию downcase_file_names, которая принимает на вход директорию
(объект-дерево), приводит имена всех файлов (только файлов - не директорий)
в этой и во всех вложенных директориях к нижнему регистру. Результат в виде
обработанной директории возвращается наружу.
"""
import copy
from fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


def downcase_file_names(node):
    name = get_name(node)
    new_meta = copy.deepcopy(get_meta(node))
    if is_file(node):
        return mkfile(name.lower(), new_meta)
    return mkdir(name,
                list(map(downcase_file_names,
                get_children(node))), new_meta)


tree = mkdir('/', [
    mkdir('eTc', [
        mkdir('NgiNx', [], {'size': 4000}),
        mkdir(
            'CONSUL',
            [mkfile('config.JSON', {'uid': 0})],
        ),
    ]),
    mkfile('HOSTS'),
])
print(tree)
print()

new_tree = downcase_file_names(tree)
print(new_tree)
print()

new_file = get_children(new_tree)[1]
get_name(new_file)