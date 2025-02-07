# https://ru.hexlet.io/courses/python-trees/lessons/accumulator/exercise_unit
# https://ru.hexlet.io/code_reviews/353882

# Аккумулятор
# ============
"""
Реализуйте функцию find_files_by_name, которая принимает на вход файловое
дерево и подстроку, а возвращает список файлов, имена которых содержат эту
подстроку. Функция должна вернуть полные пути файлам.
"""

import os
import fs
from fs import flatten, get_children, get_name, is_file, mkdir, mkfile


# Версия учителя
def find_files_by_name(tree, sample):

    def helper(node, path):
        name = get_name(node)
        full_name = os.path.join(path, name)
        if is_file(node):
            if sample in name:
                return full_name
            return []
        return flatten(list(map(lambda node: helper(node, full_name), get_children(node))))

    return helper(tree, "")


tree = mkdir('/', [
    mkdir('etc', [
        mkdir('apache'),
        mkdir('nginx', [
            mkfile('nginx.conf', {'size': 800}),
        ]),
        mkdir('consul', [
            mkfile('config.json'),
            mkfile('data'),
            mkfile('raft'),
        ]),
    ]),
    mkfile('hosts', {'size': 3500}),
    mkfile('resolve', {'size': 1000}),
])
print(find_files_by_name(tree, 'co'))
# ['/etc/nginx/nginx.conf', '/etc/consul/config.json']

