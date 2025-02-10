from pathlib import Path

from functions import get_function

# функция, которую нужно протестировать
to_html_list = get_function()

input_data_files = 'list.csv', 'list.json', 'list.yaml'
result_html_file = 'result.html'


def get_full_path(filename):
    return Path(__file__).parent / 'test_data' / filename


# BEGIN (write your solution here)
def test_to_html_list():
    full_result_html_path = get_full_path(result_html_file)
    result_html_content = full_result_html_path.read_text()
    for file in input_data_files:
        full_input_data_path = get_full_path(file)
        assert to_html_list(full_input_data_path) == result_html_content
# END
