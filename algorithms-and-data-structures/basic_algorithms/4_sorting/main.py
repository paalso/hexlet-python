#!/usr/bin/env python3

from sorting import (
    bubble_sort,
    bubble_sort_hexlet,
    selection_sort,
    quick_sort
)


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
    # test_sorting(bubble_sort)
    # test_sorting(bubble_sort_hexlet)
    # test_sorting(selection_sort)
    test_sorting(quick_sort)

    # L = [2, 8, 1, 2, 4, 5, 1, 3, 0]
    # L = [10, 8, 4, 7, 9, 6, 5]
    # L = [5, 4, 10, 1, 8, 2, 7, 9, 6, 3, 4]
    # L = [1, 2, 3, 4, 5]
    # L = [7, 6, 5, 4, 3, 2, 1]
    # L = [1, 6, 5, 2, 2, 4, 8]
    
    # print(f'Before:\n', *L)
    
    # pivot = 2
    # partition(L, 0, len(L) - 1, pivot)

    # sort_subarray(L, 0, len(L) - 1)
    
    # print(f'After:\n', *L)


if __name__ == '__main__':
    main()
