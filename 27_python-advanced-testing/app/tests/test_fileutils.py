import os, pytest

from src.fileutils import read, get_files_count


existing_file_path = 'test_data/if.txt'
non_existing_path = '/undefined'
existing_dir_path = '/etc'
dir_to_count_files_flat = 'test_data/fixtures/flat'
dir_to_count_files_nested = 'test_data/fixtures/nested'
fake_logger = lambda: None


def get_fixture_path(name):
    return os.path.join('test_data/fixtures', name)


def test_correct_read():
    result = read(existing_file_path)
    assert len(result) > 0
    assert result[:2] == 'If'


def test_non_existing_path_read():
    with pytest.raises(FileNotFoundError):
        assert read(non_existing_path)


def test_existing_dir_path_read():
    with pytest.raises(IsADirectoryError):
        assert read(existing_dir_path)


def test_get_files_count():
    directory_path = get_fixture_path("nested")
    files_count = get_files_count(directory_path, lambda: None)
    assert files_count == 4
