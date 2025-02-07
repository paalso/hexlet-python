import pytest
from hexlet_pytest.get_files_count import get_files_count
from unittest.mock import Mock


def get_fixture_path(name):
    return os.path.join('fixtures', name)


def logger(*args):
    pass


def test_get_files_count():
    assert get_files_count(
        'tests/fixtures/get_files_count_fixtutes/flat', log=logger) == 2
    assert get_files_count(
        'tests/fixtures/get_files_count_fixtutes/nested', log=logger) == 4


def test_get_files_count_ligging():
    mock_logger = Mock()
    get_files_count(
        'tests/fixtures/get_files_count_fixtutes/flat', log=mock_logger)

    assert mock_logger.call_count == 1
    mock_logger.assert_any_call('Go!')
    assert mock_logger.call_args.args[0] == 'Go!'
