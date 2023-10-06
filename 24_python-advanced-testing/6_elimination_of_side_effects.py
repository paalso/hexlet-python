# https://ru.hexlet.io/courses/python-advanced-testing/lessons/elimination-of-side-effects/exercise_unit
# https://ru.hexlet.io/code_reviews/1170591

# Python: Продвинутое тестирование
# 6. Инверсия зависимостей

'''
Протестируйте функцию get_files_count(), которая считает количество всех
файлов в указанной директории и всех поддиректориях

У этой функции есть дополнительное поведение. Во время обхода файлов она
записывает информацию о задействованных файлах в специальный файл —
журнал действий (лог).
'''

import os
from functions import get_function

get_files_count = get_function()


def logger():
    pass


# BEGIN (write your solution here)
def test_get_files_count():
    assert get_files_count(
        'fixtures/flat', log=logger) == 2
    assert get_files_count(
        'fixtures/nested', log=logger) == 4
# END


# Hexlet's version
# BEGIN
# def get_fixture_path(name):
#     return os.path.join('fixtures', name)


# def test_get_files_count():
#     # flat можно не тестировать так как nested покрывает и flat тоже
#     directory_path = get_fixture_path("nested")
#     files_count = get_files_count(directory_path, lambda: None)
#     assert files_count == 4
# END
