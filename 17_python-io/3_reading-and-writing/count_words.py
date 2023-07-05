# https://ru.hexlet.io/courses/python-io/lessons/reading-and-writing/exercise_unit
# https://ru.hexlet.io/code_reviews/1072026
# Python: Основы текстового ввода-вывода -> Запись и чтение

# Реализуйте функцию count_words(), которая принимает на вход путь до
# текстового файла, и возвращает словарь частот встречающихся слов.
# При подсчете слов не учитывайте регистр.

import collections
import string


def count_words(filemame):
    f = open(filemame, "r")
    words = f.read().lower().split()
    words_cleared_from_punctuation = map(
        lambda word: word.rstrip(string.punctuation), words
    )
    return collections.Counter(words_cleared_from_punctuation)


print(count_words('python.txt'))
print()
print(count_words('io.txt'))
