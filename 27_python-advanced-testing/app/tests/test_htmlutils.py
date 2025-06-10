import os
import shutil

from src.htmlutils import prettify_html_file
# from pytest import tm


def read(file_path):
    with open(file_path, "r") as f:
        result = f.read()
    return result


def get_test_data_path(name):
    return os.path.join("test_data", name)


def prettify_html_file(tmp_path):
    before_path = get_test_data_path('before.html')
    path_to_process = shutil.copy(before_path, tmp_path)
    prettify_html_file(path_to_process)
    expected_content = read(get_test_data_path('after.html'))
    assert read(path_to_process) == expected_content


'''
# https://ru.hexlet.io/code_reviews/1166413

@pytest.fixture(scope="module")
def expected():
    return read(get_test_data_path("after.html"))


# Подготавливаем фикстуру с файлом источником
@pytest.fixture
def dest_file(tmp_path):
    dest = tmp_path / "before.html"
    shutil.copyfile(get_test_data_path("before.html"), dest)
    return dest


def test_prettify(dest_file, expected):
    prettify_html_file(dest_file)
    actual = read(dest_file)
    assert actual == expected
'''