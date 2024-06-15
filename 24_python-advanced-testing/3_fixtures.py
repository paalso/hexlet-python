# https://ru.hexlet.io/courses/python-advanced-testing/lessons//exercise_unit
# https://ru.hexlet.io/code_reviews/1163429

# Python: Объектно-ориентированный дизайн Продвинутое тестирование
# 3. Фикстуры

# Протестируйте функцию, которая преобразует входные форматы в выходной HTML.
# На вход она поддерживает форматы YML, JSON и CSV:


from functions import get_function
import os

to_html_list = get_function()


# BEGIN (write your solution here)
import pytest

INPUT_FILES = 'list.json', 'list.yaml', 'list.csv'


@pytest.fixture
def expected_html():
    with open('fixtures/result.html') as f:
        return f.read().strip()


@pytest.mark.parametrize("file", INPUT_FILES)
def test_json_to_html_parser(file, expected_html):
    path = os.path.join('fixtures', file)
    result = to_html_list(path)
    assert expected_html == result
# END

