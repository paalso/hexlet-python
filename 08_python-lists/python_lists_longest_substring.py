# https://https://ru.hexlet.io/challenges/python_lists_longest_substring_exercise
# https://ru.hexlet.io/code_reviews/210503

# Python: Самая длинная подстрока
# ================================
# Реализуйте функцию find_longest_length, принимающую на вход строку и
# возвращающую длину максимальной последовательности из неповторяющихся
# символов. Подстрока может состоять из одного символа. Например в строке
# qweqrty, можно выделить следующие подстроки: qwe, weqrty. Самой длинной
# будет weqrty, а её длина — 6 символов.


def find_longest_length(text):
    size = len(text)

    if size == 0:
        return 0

    def find_longest_length_from(pos):
        chars = set([text[pos]])
        i = pos + 1
        while i < size:
            if (c := text[i]) in chars:
                return i - pos
            chars.add(c)
            i += 1
        return size - pos

    def find_longest_length_from1(pos):
        chars = [text[pos]]
        i = pos + 1
        while i < size:
            if (c := text[i]) in chars:
                return i - pos
            chars.append(c)
            i += 1
        return size - pos

    return max(map(find_longest_length_from1, range(size)))
    return max(map(find_longest_length_from, range(size)))


assert find_longest_length('') == 0
assert find_longest_length('a') == 1
assert find_longest_length('abcdeef') == 5
assert find_longest_length('jabjcdel') == 7


def unique_sequence_length(string):
    unique_sequence = []
    for char in string:
        if char not in unique_sequence:
            unique_sequence.append(char)
        else:
            return len(unique_sequence)
    return len(unique_sequence)


def find_longest_length1(string):
    longest_length = 0
    for i in range(len(string)):
        substr_length = unique_sequence_length(string[i:])
        if longest_length < substr_length:
            longest_length = substr_length
    return longest_length


def find_longest_length2(text):

    def longest_from_pos(pos):
        uniq_letters = set()
        i = 0
        for c in text[pos:]:
            if c in uniq_letters:
                return i
            uniq_letters.add(c)
            i += 1
        return i

    textlen = len(text)
    max_len = 0
    max_str = ''
    i = 0
    while i < textlen - max_len + 1:
        next_len = longest_from_pos(i)
        if next_len > max_len:
            max_len = next_len
            max_str = text[i:max_len]
        i += 1
    return max_len

# === Benchmarking =======================================================

text = \
"""Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad ipsa libero
aut quo laudantium iusto quibusdam aspernatur eveniet officiis. Rem saepe
consequatur deserunt corporis vitae consequuntur sint maxime vel ipsam!"""


def get_duration(func, *args, N=10000):
    import time
    start_time = time.time()
    for _ in range(N):
        func(*args)
    return time.time() - start_time


print(get_duration(find_longest_length, text))
print(get_duration(find_longest_length1, text))
print(get_duration(find_longest_length2, text))
