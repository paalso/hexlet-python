#!/usr/bin/env python3

# https://ru.hexlet.io/courses/basic-algorithms
# https://ru.hexlet.io/code_reviews/1315034

# Основы алгоритмов и структур данных 
# Испытание: Слияние массивов 
'''
Функция принимает два параметра: отсортированные списки arr1 и arr2,
и возвращает объединенный отсортированный список
'''

def merge(array1, array2):
    i = j = 0
    size1 = len(array1)
    size2 = len(array2)
    result = []

    while i < size1 and j < size2:
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1

    result.extend(array1[i:])
    result.extend(array2[j:])

    return result


def test():
    arr1 = [1, 2, 4, 7, 9]
    arr2 = [3, 4, 5, 8, 9, 11]
    assert merge(arr1, arr2) == [1, 2, 3, 4, 4, 5, 7, 8, 9, 9, 11]

    arr1 = [1, 2, 3, 3, 4, 4, 7, 9]
    arr2 = [3, 4, 5, 5, 8, 9, 11, 12]
    assert merge(arr1, arr2) == [1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 7, 8, 9, 9, 11, 12]

    arr1 = [1, 2, 4, 7]
    arr2 = [3, 4, 5, 6]
    assert merge(arr1, arr2) == [1, 2, 3, 4, 4, 5, 6, 7]


def main():
    test()


if __name__ == '__main__':
    main()
