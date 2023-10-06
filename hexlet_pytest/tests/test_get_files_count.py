import pytest
from hexlet_pytest.get_files_count import get_files_count


def logger():
    pass


def test_get_files_count():
    assert get_files_count(
        'tests/fixtures/get_files_count_fixtutes', log=logger) == 6
    assert get_files_count(
        'tests/fixtures/get_files_count_fixtutes/flat', log=logger) == 2
    assert get_files_count(
        'tests/fixtures/get_files_count_fixtutes/nested', log=logger) == 4
