# https://ru.hexlet.io/challenges/python_io_line_by_line_exercise/instance
# https://ru.hexlet.io/code_reviews/1077759

# Реализуйте функцию grep, принимающую на вход два параметра: подстроку для
# сопоставления и шаблон в формате glob, по которому будет происходить поиск.
# Функция должна вернуть список всех строк файлов, в которых содержится
# подстрока. Поиск должен производиться по всем файлам переданного шаблона.
# Поиск не должен учитывать файлы в поддиректориях.

import glob
import os


def get_lines_by_template(filename, template_string):
    with open(filename, 'r') as f:
        return [line for line in f if line.find(template_string) >= 0]


def grep(template_string, template_path):
    all_found_lines = []
    for path in glob.glob(template_path):
        if os.path.isfile(path):
            all_found_lines.extend(get_lines_by_template(path, template_string))
    return all_found_lines


print(grep('fox', './*'))
