import pytest
import os
import shutil

from hexlet_pytest.prettify_html_file import prettify_html_file

FILES_TO_CLEAN = [
    'tests/fixtures/test.html',
]
filepath = 'tests/fixtures/test.html'


# Будет вызываться для каждого теста
@pytest.fixture(autouse=True)
def clean_files():
    if os.path.isfile(filepath):
        os.remove(filepath)
    yield


def test_prettify_html_file():
    shutil.copy('tests/fixtures/before.html', 'tests/fixtures/test.html')
    prettify_html_file('tests/fixtures/test.html')
    processed = open('tests/fixtures/test.html', 'r').read()
    sample = open('tests/fixtures/after.html', 'r').read()
    assert processed == sample
