import copy
import fs
from fs import get_children, get_name, is_file, is_directory, mkdir, mkfile


def get_files_count(node):
    """
    Подсчёт количества файлов внутри директории
    """
    if is_file(node):
        return 1
    return sum(map(get_files_count, get_children(node)))


def get_subdirectories_info(node):
    """
    Возвращает список директорий первого уровня вложенности и количество файлов
    внутри каждой из них
    """
    if is_file(node):
        return
    return list(map(lambda node: (get_name(node), get_files_count(node)),
                    filter(is_directory, get_children(node))))


tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkdir('apache'),
        fs.mkdir('nginx', [
            fs.mkfile('nginx.conf'),
        ]),
    ]),
    fs.mkdir('consul', [
        fs.mkfile('config.json'),
        fs.mkfile('file.tmp'),
        fs.mkdir('data'),
    ]),
    fs.mkfile('hosts'),
    fs.mkfile('resolve'),
])

print(get_subdirectories_info(tree))
# [('etc', 1), ('consul', 2)]