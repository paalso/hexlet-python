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

from fs import get_children, get_meta, get_name, is_file, mkdir, mkfile
import pprint
import copy


def ls(tree):
    return list(map(lambda path: get_name(path), get_children(tree)))


def get_extension(path):
    name = get_name(path)
    point_pos = name.rfind('.')
    if point_pos > -1:
        return name[point_pos + 1:]


def is_picture(file, extensions=['jpg']):
    return is_file(file) and get_extension(file) in extensions


def compress_image(file, factor=0.5):
    name = get_name(file)
    meta = copy.deepcopy(get_meta(file))
    if is_picture(file) and 'size' in meta:
        meta['size'] = int(factor * meta['size'])
    return mkfile(name, meta)


def compress_images(tree, factor=0.5):
    name = get_name(tree)
    meta = copy.deepcopy(get_meta(tree))
    children = [compress_image(path) if is_file(path) else
                compress_images(path) for path in get_children(tree)]
    return mkdir(name, children, meta)


# tree = mkdir(
#     'my documents',
#     [
#         mkfile('avatar.jpg', {'size': 100}),
#         mkfile('photo.jpg', {'size': 150}),
#         mkfile('text.txt', {'size': 200}),
#         mkdir('subdir', [
#             mkdir('empty_subdir', []),
#             mkfile('pictire.jpg', {'size': 200})
#             ])
#     ],
#     {'hide': False}
# )

tree = mkdir(
    'my documents',
    [
        mkfile('avatar.jpg', {'size': 100}),
        mkfile('photo.jpg', {'size': 150}),
    ],
    {'hide': False}
)

pprint.pprint(tree)
print()
pprint.pprint(compress_images(tree))
