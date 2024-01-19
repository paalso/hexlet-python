#!/usr/bin/env python3

# https://ru.hexlet.io/courses/basic-algorithms/lessons/binary-search/theory_unit
# https://ru.hexlet.io/courses/basic-algorithms/lessons/recursion/theory_unit


def sgn(x):
    if x == 0:
        return 0
    if x < 0:
        return -1
    return 1


def binary_search_classical(collection, item):
    first_id = 0
    last_id = len(collection) - 1
    while first_id <= last_id:
        middle_id = (first_id + last_id) // 2
        if collection[middle_id] == item:
            return middle_id
        if item < collection[middle_id]:
            last_id = middle_id - 1
        else:
            first_id = middle_id + 1
    return -1


def binary_search_recursion(items, value):

    def helper(first_id, last_id):
        if last_id < first_id:
            return -1

        middle_id = (first_id + last_id) // 2
        if items[middle_id] == value:
            return middle_id
        if value < items[middle_id]:
            return helper(first_id, middle_id - 1)
        return helper(first_id + 1, last_id)

    return helper(0, len(items) - 1)


def binary_search_pro(collection, item, comparator):
    first_id = 0
    last_id = len(collection) - 1
    while first_id <= last_id:
        middle_id = (first_id + last_id) // 2
        if comparator(collection[middle_id], item) == 0:
            return middle_id
        if comparator(item, collection[middle_id]) < 0:
            last_id = middle_id - 1
        else:
            first_id = middle_id + 1
    return -1


def test_binary_search(binary_search_version):
    binary_search = binary_search_version
    assert binary_search([1, 2, 8, 9, 10, 10, 14], 6) == -1
    assert binary_search([1, 2, 8, 9, 10, 10, 14], 8) == 2
    assert binary_search([1, 2, 8, 9, 10, 10, 14], 1) == 0
    assert binary_search([1, 2, 8, 9, 10, 10, 14], 14) == 6
    
    assert binary_search([1, 2, 8], 1) == 0
    assert binary_search([1, 2, 8], 2) == 1
    assert binary_search([1, 2, 8], 8) == 2
    assert binary_search([1, 2, 8], 9) == -1
    assert binary_search([1, 2, 8], 3) == -1
    
    assert binary_search([1, 2], 1) == 0
    assert binary_search([1, 2], 2) == 1
    assert binary_search([1, 2], 3) == -1
    
    assert binary_search([1], 1) == 0
    assert binary_search([1], 2) == -1
    
    assert binary_search([], 0) == -1


def test_binary_search_pro(comparator):
    assert binary_search_pro([1, 2, 8, 9, 10, 10, 14], 6, comparator) == -1
    assert binary_search_pro([1, 2, 8, 9, 10, 10, 14], 8, comparator) == 2
    assert binary_search_pro([1, 2, 8, 9, 10, 10, 14], 1, comparator) == 0
    assert binary_search_pro([1, 2, 8, 9, 10, 10, 14], 14, comparator) == 6
    
    assert binary_search_pro([1, 2, 8], 1, comparator) == 0
    assert binary_search_pro([1, 2, 8], 2, comparator) == 1
    assert binary_search_pro([1, 2, 8], 8, comparator) == 2
    assert binary_search_pro([1, 2, 8], 9, comparator) == -1
    assert binary_search_pro([1, 2, 8], 3, comparator) == -1
    
    assert binary_search_pro([1, 2], 1, comparator) == 0
    assert binary_search_pro([1, 2], 2, comparator) == 1
    assert binary_search_pro([1, 2], 3, comparator) == -1
    
    assert binary_search_pro([1], 1, comparator) == 0
    assert binary_search_pro([1], 2, comparator) == -1
    
    assert binary_search_pro([], 0, comparator) == -1

    assert binary_search_pro(['aa', 'aaa', 'ac', 'dfj', 'fvd', 'js', 'sd'], 'aa', comparator) == 0
    assert binary_search_pro(['aa', 'aaa', 'ac', 'dfj', 'fvd', 'js', 'sd'], 'aaa', comparator) == 1
    assert binary_search_pro(['aa', 'aaa', 'ac', 'dfj', 'fvd', 'js', 'sd'], 'ac', comparator) == 2
    assert binary_search_pro(['aa', 'aaa', 'ac', 'dfj', 'fvd', 'js', 'sd'], 'sd', comparator) == 6
    assert binary_search_pro(['aa', 'aaa', 'ac', 'dfj', 'fvd', 'js', 'sd'], 'aaaa', comparator) == -1
    assert binary_search_pro(['aa', 'aaa', 'ac', 'dfj', 'fvd', 'js', 'sd'], 'sz', comparator) == -1



def comparator(s1, s2):
    if s1 == s2:
        return 0
    if s1 < s2:
        return -1
    return 1


def main():
    test_binary_search(binary_search_classical)
    test_binary_search(binary_search_recursion)
    test_binary_search_pro(comparator)


if __name__ == '__main__':
    main()
