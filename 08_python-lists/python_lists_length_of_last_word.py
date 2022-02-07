# https://ru.hexlet.io/challenges/python_lists_length_of_last_word_exercise
# https://ru.hexlet.io/code_reviews/206988

# Python: Длина последнего слова
# ===============================

# Реализуйте функцию length_of_last_word, которая возвращает длину последнего
# слова переданной на вход строки. Словом считается любая последовательность,
# не содержащая пробелов.


def length_of_last_word(text):
    words = text.split()
    if not words:
        return 0
    return len(words[-1])


assert length_of_last_word('') == 0
assert length_of_last_word('   ') == 0
assert length_of_last_word('man') == 3
assert length_of_last_word('man in Black') == 5
assert length_of_last_word('hello, world!     ') == 6
