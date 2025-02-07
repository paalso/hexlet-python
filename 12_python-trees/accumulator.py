import copy
import fs
from fs import get_children, get_name, is_file, is_directory, mkdir, mkfile, flatten


def find_empty_dir_paths(tree, max_depth=0):
    if is_file(tree):
        return

    def helper(tree, depth):
        if depth > max_depth:
            return []

        children = get_children(tree)
        if len(children) == 0:
            return get_name(tree)
        children_dirs = filter(is_directory, children)
        return list(map(lambda tree: helper(tree, depth + 1), children_dirs))

    return flatten(helper(tree, 0))


tree = fs.mkdir('/', [
    fs.mkdir('etc', [
        fs.mkdir('apache'),
        fs.mkdir('nginx', [
            fs.mkfile('nginx.conf'),
        ]),
        fs.mkdir('consul', [
            fs.mkfile('config.json'),
            fs.mkdir('data'),
        ]),
    ]),
    fs.mkdir('logs'),
    fs.mkfile('hosts'),
])

print(find_empty_dir_paths(tree, 2))

empty_tree = fs.mkdir('/', [])
print(find_empty_dir_paths(empty_tree))

file_tree = fs.mkfile('somefile')
print(find_empty_dir_paths(file_tree))


