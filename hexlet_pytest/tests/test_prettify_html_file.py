
import pytest
import os
import shutil

from hexlet_pytest.prettify_html_file import prettify_html_file


# Фикстура для копирования before.html в test.html перед тестом
@pytest.fixture
def copy_before_html():
    shutil.copy('tests/fixtures/before.html', 'tests/fixtures/test.html')
    yield  # Этот блок выполняется после завершения теста
    # Выполните действия после завершения теста (например, удаление test.html)
    os.remove('tests/fixtures/test.html')


# Версия 1
def test_prettify_html_file1(copy_before_html):
    # Преобразуем test.html и сравниваем с эталонным after.html
    prettify_html_file('tests/fixtures/test.html')
    result_content = open('tests/fixtures/test.html', 'r').read()
    expected_content = open('tests/fixtures/after.html', 'r').read()
    assert result_content == expected_content


# Версия 2
def test_prettify_html_file2(tmp_path):
    # Создаем временный файл с содержимым before.html
    input_file = tmp_path / "test.html"
    shutil.copy('tests/fixtures/before.html', input_file)

    # Преобразуем test.html и сравниваем с эталонным after.html
    prettify_html_file(input_file)
    result_content = input_file.read_text()
    expected_content = open("tests/fixtures/after.html", "r").read()
    assert result_content == expected_content
