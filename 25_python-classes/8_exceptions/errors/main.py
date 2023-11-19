#!/usr/bin/env python3

from FileError import FileError
from NotExistsError import NotExistsError

def process(x):
    if x == 1:
        raise NotExistsError('ERROR! NotExistsError!')
    return x


def main():
    print('x = ', end='')
    x = int(input())
    try:
        result = 10 / process(x)
        print(result)
    except FileError as e:
        print(e)


if __name__ == '__main__':
    main()
