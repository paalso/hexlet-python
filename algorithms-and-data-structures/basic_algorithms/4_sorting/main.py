#!/usr/bin/env python3

from sorting import bubble_sort, bubble_sort_hexlet, selection_sort


def test_sorting(sort_function):
    items = []
    sort_function(items)
    assert items == []

    items = [1]
    sort_function(items)
    assert items == [1]

    items = [2, 1]
    sort_function(items)
    assert items == [1, 2]

    items = [4, 3, 2, 1]
    sort_function(items)
    assert items == [1, 2, 3, 4]

    items = [4, 3, 3, 4, 2, 1, 5]
    sort_function(items)
    assert items == [1, 2, 3, 3, 4, 4, 5]

    items = [1, 2, 3, 4]
    sort_function(items)
    assert items == [1, 2, 3, 4]


def main():
    test_sorting(bubble_sort)
    test_sorting(bubble_sort_hexlet)
    test_sorting(selection_sort)


if __name__ == '__main__':
    main()
