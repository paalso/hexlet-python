import pytest
from hexlet_pytest.to_html_list import to_html_list
import os

PATH_PREFIX = 'tests/fixtures/'


@pytest.fixture
def html():
    path_html = os.path.join(PATH_PREFIX, 'result.html')
    with open(path_html) as f_html:
        return f_html.read().rstrip()


def test_to_html_list_from_csv(html):
    path_csv = os.path.join(PATH_PREFIX, 'list.csv')
    print(html)
    assert to_html_list(path_csv) == html


def test_to_html_list_from_json(html):
    path_csv = os.path.join(PATH_PREFIX, 'list.json')
    assert to_html_list(path_csv) == html


def test_to_html_list_from_yaml(html):
    path_yaml = os.path.join(PATH_PREFIX, 'list.yaml')
    assert to_html_list(path_yaml) == html
