# https://ru.hexlet.io/courses/python-advanced-testing/lessons/files/exercise_unit
# https://ru.hexlet.io/code_reviews/1166413

# Python: Продвинутое тестирование
# 5. Тестирование кода, взаимодействующего с файлами

# Протестируйте функцию, которая форматирует и изменяет указанный HTML-файл:

import os
import pytest
import shutil
from functions import get_function

prettify_html_file = get_function()


# BEGIN (write your solution here)
# Фикстура для копирования before.html в test.html перед тестом
@pytest.fixture
def copy_before_html():
    shutil.copy('fixtures/before.html', 'fixtures/test.html')
    yield  # Этот блок выполняется после завершения теста
    os.remove('fixtures/test.html')


def test_prettify_html_file(copy_before_html):
    prettify_html_file('fixtures/test.html')
    processed = open('fixtures/test.html', 'r').read()
    sample = open('fixtures/after.html', 'r').read()
    assert processed == sample
# END


# Hexlet's version
# BEGIN
def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def get_fixture_path(name):
    return os.path.join('fixtures', name)


file_name = 'before.html'
src = get_fixture_path(file_name)


@pytest.fixture(scope='module')
def expected():
    return read(get_fixture_path('after.html'))


@pytest.fixture
def dest_file(tmpdir):
    dest = tmpdir.join(file_name)
    shutil.copyfile(src, dest)
    return dest


def test_prettify(dest_file, expected):
    prettify_html_file(dest_file)
    actual = read(dest_file)
    assert actual == expected
# END
