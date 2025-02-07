# https://ru.hexlet.io/courses/python-declarative-programming/lessons/generator-expressions/exercise_unit
# https://ru.hexlet.io/code_reviews/435985

# Генераторные выражения
# =======================

# реализовать функцию length_frequencies(), которая принимает
# последовательность (iterable) слов (строк) в качестве единственного
# аргумента и возвращает словарь, ключами которого выступают длины слов,
# а значениями — количество слов соответствующей длины.


from itertools import groupby


def length_frequencies(items):
    return {len_: len(list(group))
            for len_, group in groupby(sorted(items, key=len), key=len)}


print(length_frequencies(['a', 'bb', 'ccc', 'a']))
