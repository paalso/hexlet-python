# https://ru.hexlet.io/courses/python-trees/lessons/manipulations/exercise_unit
# https://ru.hexlet.io/code_reviews/347621

# Манипуляции с виртуальной файловой системой
# ============================================

"""
Реализуйте функцию compress_images(), которая принимает на вход директорию,
находит внутри нее картинки и "сжимает" их. Под сжиманием понимается уменьшение
свойства size в метаданных в два раза. Функция должна вернуть обновленную
директорию со сжатыми картинками и всеми остальными данными, которые были
внутри этой директории.
Картинками считаются все файлы, заканчивающиеся на .jpg.
"""

import copy
import fs
from fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


def is_image(node):
    return is_file(node) and get_name(node).endswith('.jpg')


def compress_image(node):
    new_meta = copy.deepcopy(get_meta(node))
    if is_image(node):
        new_meta['size'] //= 2
        return mkfile(get_name(node), new_meta)
    return node


def compress_images(tree):
    new_children = list(map(
            lambda e: compress_image(e) if is_file(e) else compress_images(e),
                   get_children(tree)))
    return mkdir(get_name(tree), new_children, copy.deepcopy(get_meta(tree)))


tree = mkdir(
    'my documents',
    [
        mkfile('avatar.avi', {'size': 21000}),
        mkfile('avatar.jpg', {'size': 100}),
        mkfile('photo.jpg', {'size': 150}),
    ],
    {'hide': False}
)


print(compress_images(tree))