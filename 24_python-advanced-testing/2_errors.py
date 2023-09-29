# https://ru.hexlet.io/courses/python-advanced-testing/lessons//exercise_unit

# Python: Объектно-ориентированный дизайн Продвинутое тестирование
# 2. Тестирование ошибок

# В этом задании вам предстоит работать с функцией read(), которая читает
# содержимое файла. Напишите негативный тест этой функции, проверяющий
# ошибочные ситуации. Рассмотрите следующие ситуации:
#     Файл не найден
#     В функцию передан путь до директории read(filepath)

import pytest
from functions import get_function

read = get_function()


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        read('/undefined')


def test_read_with_directory():
    with pytest.raises(IsADirectoryError):
        read('/etc')
