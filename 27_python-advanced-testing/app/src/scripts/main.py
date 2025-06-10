import os
from src.fileutils import get_files_count


def main():
    fake_logger = lambda: None
    input_path = 'test_data/fixtures'
    print(get_files_count(input_path, fake_logger))

    input_path = 'test_data/fixtures/flat'
    print(get_files_count(input_path, fake_logger))

    input_path = 'test_data/fixtures/nested'
    print(get_files_count(input_path, fake_logger))


if __name__ == "__main__":
    main()
