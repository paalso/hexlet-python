# https://ru.hexlet.io/challenges/python_functions_filter_anagrams
# https://ru.hexlet.io/code_reviews/257369

# Python: Функции → Фильтр анаграмм

# Реализуйте функцию filter_anagrams, которая находит все слова-анаграммы.
# Функция принимает исходное слово и последовательность (iterable) слов для
# проверки, а возвращает последовательность анаграмм.


def filter_anagrams(sample, items):
    normalized_sample = sorted(sample)
    return filter(lambda e: sorted(e) == normalized_sample, items)


assert list(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])) == ['aabb', 'bbaa']
assert list(filter_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])) == ['carer', 'racer']
assert list(filter_anagrams('laser', ['lazing', 'lazy',  'lacer'])) == []
assert list(filter_anagrams([1, 2], [[2, 1], [2, 2], [1, 2]])) == [[2, 1], [1, 2]]
