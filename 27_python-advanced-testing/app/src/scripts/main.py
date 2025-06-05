import os
from src.fileutils import read
from src.utils import get_fake_data


def main():
    print(get_fake_data({'first_name': 'Вася', 'last_name': 'Пупкин'}))


if __name__ == "__main__":
    main()
