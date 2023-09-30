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

PATH_PREFIX = '/usr/src/app/fixtures/'


@pytest.fixture
def html():
    path_html = os.path.join(PATH_PREFIX, 'result.html')
    with open(path_html) as f_html:
        return f_html.read().rstrip()


def test_to_html_list_from_csv(html):
    path_csv = os.path.join(PATH_PREFIX, 'list.csv')
    assert to_html_list(path_csv) == html


def test_to_html_list_from_json(html):
    path_csv = os.path.join(PATH_PREFIX, 'list.json')
    assert to_html_list(path_csv) == html


def test_to_html_list_from_yaml(html):
    path_yaml = os.path.join(PATH_PREFIX, 'list.yaml')
    assert to_html_list(path_yaml) == html
# END
