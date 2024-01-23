# https://ru.hexlet.io/courses/python-advanced-testing/lessons//exercise_unit
# https://ru.hexlet.io/code_reviews/1294635

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
        

# Another version
def test_non_existing_path_file_read_error():
    non_existing_path = 'non-existing-path'

    with pytest.raises(FileNotFoundError) as e:
        file_read(non_existing_path)

    error_message_pattern = f"No such file or directory: '{non_existing_path}'"
    assert  error_message_pattern in str(e.value)


def test_directory_path_file_read_error():
    tmp_dir = 'tmp-dir'
    os.mkdir(tmp_dir)

    with pytest.raises(IsADirectoryError) as e:
        file_read(tmp_dir)
    
    os.rmdir(tmp_dir)

    error_message_pattern = f"Is a directory: '{tmp_dir}'"
    assert  error_message_pattern in str(e.value)

