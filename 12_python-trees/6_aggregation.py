# https://ru.hexlet.io/courses/python-trees/lessons/aggregation/exercise_unit
# https://ru.hexlet.io/code_reviews/352571

# Аггрегация
# ===========
"""
Реализуйте функцию get_hidden_files_count, которая считает количество скрытых
файлов в директории и всех поддиректориях. Скрытым файлом в Linux системах
считается файл, название которого начинается с точки.
"""

import copy
from fs import get_children, get_name, is_file, mkdir, mkfile


def get_nodes_count(node):
    if is_file(node):
        return 1
    return sum(map(lambda e: get_nodes_count(e), get_children(node))) + 1


def is_hidden(node):
    return get_name(node).startswith('.')


def get_hidden_files_count(node):
    if is_file(node):
        return is_hidden(node)

    return sum(map(get_hidden_files_count, get_children(node)))


tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('.nginx.conf', {'size': 800}),
        ]),
        mkdir('.consul', [
            mkfile('.config.json', {'size': 1200}),
            mkfile('data', {'size': 8200}),
            mkfile('raft', {'size': 80}),
        ]),
     ]),
     mkfile('.hosts', {'size': 3500}),
     mkfile('resolve', {'size': 1000}),
])


print(get_hidden_files_count(tree))


'''
def get_nodes_count(node):
    if is_file(node):
        return 1
    return sum(map(lambda e: get_nodes_count(e), get_children(node))) + 1


tree = mkdir('/', [
    mkdir('etc', [
        mkfile('bashrc'),
        mkfile('consul.cfg'),
    ]),
    mkfile('hexletrc'),
    mkdir('bin', [
        mkfile('ls'),
        mkfile('cat'),
    ]),
])


print(get_nodes_count(tree))    # 8
'''
