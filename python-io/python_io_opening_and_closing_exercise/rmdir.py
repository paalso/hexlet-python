#!/usr/bin/env python3

# https://ru.hexlet.io/challenges/python_io_opening_and_closing_exercise/instance
# https://ru.hexlet.io/code_reviews/1080240

# Python: Основы текстового ввода-вывода
# • Испытание: Удаление директорий 
# ========================================

# Реализуйте функцию rrmdir(), удаляющую директорию рекурсивно,
# то есть вместе со всем своим содержимым.

import os


def get_dirlist(path):
    """
      Return a sorted list of all entries in path.
      This returns just the names, not the full path to the names.
    """
    return sorted(os.listdir(path))


def is_dir_empty(path):
    return os.listdir(path) == []


def tree_bak(path, depth=0, prefix='| '):
    print(prefix * depth + os.path.basename(path))
    if os.path.isfile(path):
        return
    dir_content = list(map(lambda item: os.path.join(path, item),
                           os.listdir(path)))
    for item in dir_content:
        tree_bak(item, depth + 1)


def tree(path, depth=0, prefix='| '):
    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix * depth + f)
        fullname = os.path.join(path, f)
        if os.path.isdir(fullname):
            tree(fullname, depth + 1)


def rrmdir(path):
    for item in os.scandir(path):
        if os.path.isfile(item):
            os.remove(item)
        else:
            rmdir(item)
    os.rrmdir(path)


def main():
    path = 'dir_to_remove'
    rrmdir(path)


if __name__ == '__main__':
    main()
