# https://ru.hexlet.io/courses/python-functions/lessons/recursion/exercise_unit
# https://ru.hexlet.io/code_reviews/272178

# Рекурсия
# =========

# Реализовать через рекурсивный процесс:

# length() принимает список и возвращает его длину

# reverse_range() принимает два числа begin и end и возвращает перевернутый
# список всех чисел между. Для простоты договоримся, что begin <= end

# filter_positive() принимает список чисел и возвращает новый только с
# положительными элементами

def length(items):
    if items == []:
        return 0

    items.pop()
    return 1 + length(items)


def filter_positive(items):
    if items == []:
        return []

    last = items.pop()
    return filter_positive(items) + ([last] if last > 0 else [])


def reverse_range(begin, end):
    if begin == end:
        return [begin]

    return [end] + reverse_range(begin, end - 1)


def main():
    assert length([1, 2, 3]) == 3

    assert reverse_range(1, 1) == [1]
    assert reverse_range(1, 3) == [3, 2, 1]

    assert filter_positive([]) == []
    assert filter_positive([-3]) == []
    assert filter_positive([1, -2, 3]) == [1, 3]


if __name__ == '__main__':
    main()
