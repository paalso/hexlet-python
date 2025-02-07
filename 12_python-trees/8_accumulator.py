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
from fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


# Version # 1
# Классическая
def find_files_by_name(tree, substr):
    result = []

    def walk(node, path):
        if is_file(node):
            if (substr in get_name(node)):
                result.append(path)
            return

        for node in get_children(node):
            walk(node, os.path.join(path, get_name(node)))

    walk(tree, get_name(tree))
    return result


# Версия № 2
# Получше
def find_files_by_name2(tree, sample):

    found_files_by_name = []

    def helper(node, path):
        name = get_name(node)
        full_name = os.path.join(path, name)
        if is_file(node):
            if sample in name:
                found_files_by_name.append(full_name)
            return
        list(map(lambda node: helper(node, full_name), get_children(node)))

    helper(tree, "")
    return found_files_by_name


# Version # 3
# Идеальная
def find_files_by_name(tree, substr):

    def walk(node, path):
        if is_file(node):
            return path if substr in get_name(node) else []
        return flatten(map(
            lambda node: walk(node, os.path.join(path, get_name(node))),
            get_children(node)))

    return walk(tree, get_name(tree))


'''
Разница в том, что в v.2 path - это путь до текущего node, исключая его
а в v.3 - до текущего node, включая
И v.3 в общем случае работает неверно - если изменить имя корневого пути v '/'
на '/home', например:
    ['home/etc/nginx/nginx.conf', 'home/etc/consul/config.json']
    ['/etc/nginx/nginx.conf', '/etc/consul/config.json']
То, что в тестовом примере дерево каталогов начинается с '/',
с одной стороны сильно сбивает и усложняет решения, но, с другой стороны,
если пользоваться os.path - помогает
'''

tree = mkdir('home', [
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
print(find_files_by_name2(tree, 'co'))
print(find_files_by_name3(tree, 'co'))
# ['/etc/nginx/nginx.conf', '/etc/consul/config.json']
