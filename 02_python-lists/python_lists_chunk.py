# https://ru.hexlet.io/challenges/python_lists_chunk_exercise
# https://ru.hexlet.io/code_reviews/207815

# Python: Чанкование
# ===================

# Реализуйте функцию chunked, которая принимает на вход число и
# последовательность. Число которое задает размер чанка (куска). Функция
# должна вернуть список, состоящий из чанков указанной размерности. При этом
# список должен делиться на куски-списки, строка — на строки, кортеж —
# на кортежи!


def chunked(size, coll):
    return [coll[i * size:i * size + size]
            for i in range((len(coll) + size - 1) // size)]


assert chunked(2, ['a', 'b', 'c', 'd']) == [['a', 'b'], ['c', 'd']]

assert chunked(2, ['a', 'b', 'c', 'd', 'e', 'f', 'g']) == \
                  [['a', 'b'], ['c', 'd'], ['e', 'f'], ['g']]

assert chunked(3, ['a', 'b', 'c', 'd']) == [['a', 'b', 'c'], ['d']]

assert chunked(3, 'foobar') == ['foo', 'bar']

assert chunked(10, (42,)) == [(42,)]

assert chunked(2, ('a', 'b', 'c', 'd', 'e')) == [('a', 'b'), ('c', 'd'), ('e', )]


'''
def chunked(size, coll):
    chunks = []
    for i in range(len(coll), size):
        chunks.append(coll[i:i + size])
    return chunks
'''