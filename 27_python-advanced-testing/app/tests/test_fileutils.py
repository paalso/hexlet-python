import pytest

from src.fileutils import read


existing_file_path = 'data/if.txt'
non_existing_path = '/undefined'
existing_dir_path = '/etc'


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
