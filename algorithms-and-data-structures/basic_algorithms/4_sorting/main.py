#!/usr/bin/env python3

import random

from sorting import (
    bubble_sort,
    bubble_sort_hexlet,
    selection_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    quick_sort3
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

    items = [random.randint(1, 10_000) for _ in range(10)]
    items_copy = items[:]
    sort_function(items)
    items_copy.sort()
    # print(f'Sort_function: {sort_function.__name__}, result: {items == items_copy}')
    assert items == items_copy


def test_sortings():
    test_sorting(bubble_sort)
    test_sorting(bubble_sort_hexlet)
    test_sorting(selection_sort)
    test_sorting(insertion_sort)
    test_sorting(merge_sort)
    test_sorting(quick_sort)
    test_sorting(quick_sort3)


def main():
    test_sortings()

    # L = [2, 8, 1, 2, 4, 5, 1, 3, 0]
    # L = [10, 8, 4, 7, 9, 6, 5]
    # L = [1, 2, 3, 4, 5]
    # L = [7, 6, 5, 4, 3, 2, 1]
    # L = [1, 6, 5, 2, 2, 4, 8]
    # L = [5, 4, 10, 1, 8, 2, 7, 9, 6, 3, 4]
    
    # print(f'Before:\n', *L)
    
    # pivot = 2
    # partition(L, 0, len(L) - 1, pivot)

    # sort_subarray(L, 0, len(L) - 1)
    # selection_sort(L)
    # print(f' After:\n', *L)


if __name__ == '__main__':
    main()
