#!/usr/bin/env python3

import utils


def main():
    utils.read_files(['a.txt', 'b.txt', 'c.txt', 'subdir'])
    # utils.read_files(['a.txt', 'b.txt', 'c.txt'])


if __name__ == '__main__':
    main()
