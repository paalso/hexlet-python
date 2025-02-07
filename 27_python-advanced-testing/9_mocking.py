# https://ru.hexlet.io/courses/python-advanced-testing/lessons/mocking/exercise_unit
# https://ru.hexlet.io/code_reviews/1183134

# Python: Продвинутое тестирование
# 9. Мокинг

'''
Протестируйте функцию get_files_count(path, log), которая считает количество
всех файлов в указанной директории и всех поддиректориях. В отличие от
предыдущей версии задания, здесь нас интересует, что эта функция выполняет
логирование с помощью функции log(). Мы хотим убедиться, что она один раз
отправляет сообщение c текстом 'Go!' в лог. Для этого придется воспользоваться
моком.

unittest.mock.call_count
unittest.mock.call_args
Обратите внимание в документации, где именно создается мок
'''

import os
from unittest.mock import Mock
from functions import get_function

get_files_count = get_function()


def get_fixture_path(name):
    return os.path.join('fixtures', name)


# BEGIN (write your solution here)
def test_get_files_count_logging():
    mock_logger = Mock()

    get_files_count('fixtures/flat', log=mock_logger)

    assert mock_logger.call_count == 1
    mock_logger.assert_any_call('Go!')
# END

