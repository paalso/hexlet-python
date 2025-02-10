import pytest
from pathlib import Path
from functions import get_function

to_html_list = get_function()

input_data_files = 'list.csv', 'list.json', 'list.yaml'
result_html_file = 'result.html'


def get_full_path(filename):
    return Path(__file__).parent / 'test_data' / filename


@pytest.fixture(scope="module")
def expected_html():
    """Читаем эталонный HTML-файл один раз за весь тестовый запуск"""
    return get_full_path(result_html_file).read_text()


@pytest.mark.parametrize("input_file", input_data_files)
def test_to_html_list(input_file, expected_html):
    """Тестируем разные входные файлы, сравнивая с эталонным HTML"""
    input_path = get_full_path(input_file)
    assert to_html_list(input_path) == expected_html
