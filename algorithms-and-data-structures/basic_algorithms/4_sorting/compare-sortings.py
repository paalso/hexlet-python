#!/usr/bin/env python3

PROGRAMS = ['./sort1', './sort2', './sort3']
INPUT_FILES = [
    'sorted5000.txt',
    'sorted10000.txt',
    'sorted50000.txt',
    'reversed5000.txt',
    'reversed10000.txt',
    'reversed50000.txt',
    'random5000.txt',
    'random10000.txt',
    'random50000.txt',
]


def int_array_from_file(path):
    with open(path) as f:
        return [int(value.rstrip()) for value in f.readlines()]


def main():
    items = int_array_from_file('sorted5.txt')
    print(items)


if __name__ == '__main__':
    main()
