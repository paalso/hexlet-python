# https://ru.hexlet.io/challenges/python_declarative_programming_intersperse_exercise
# https://ru.hexlet.io/code_reviews/431480

# Чанкование потока
# ==================

# Реализовать функцию ichunks(), которая должна принимать в качестве
# аргументов размер кусочка (положительное целое число) и источник данных
# (итератор). Вернуть функция должна итератор списков заданной длины,
# содержащих элементы из источника данных.

from itertools import count


def ichunks(chunk_size, itarable):
    next_chunk = []
    for e in itarable:
        next_chunk.append(e)
        if len(next_chunk) == chunk_size:
            yield next_chunk
            next_chunk = []


# print(list(ichunks(1, [100, 200, 300, 400])))
# print(list(squares_plus_one(27)))
# print(ichunks(2, squares_plus_one(27)))
# print(list(ichunks(2, squares_plus_one(27))))

assert list(ichunks(1, [])) == []
assert list(ichunks(2, [42])) == []
assert list(ichunks(1, [100, 200])) == [[100], [200]]
assert list(ichunks(2, range(5))) == [[0, 1], [2, 3]]


def squares_plus_one(n):
    k = 1
    while True:
        next_ = k * k + 1
        if next_ > n:
            return
        k += 1
        yield next_


assert list(ichunks(2, squares_plus_one(27))) == [[2, 5], [10, 17]]

assert list(
    ichunks(3, ['a', 'b', 'c', 'd']),
) == [['a', 'b', 'c']]

stream = count(1000, 3)

sliced = ichunks(1, stream)

i = 0
for e in sliced:
    if i == 3:
        break
    print(e)
    i += 1


# BEGIN
# def ichunks(size, source):
#     return map(list, zip(*([iter(source)] * size)))
    # "iter(source)" получает именно итератор, даже если на вход
    # был передан iterable (строка, список).
    #
    # "[iterator] * n" размножает ссылки на итератор.
    #
    # "zip(*l)" пакует в кортежи все первые элементы из
    # списка источников "l", затем все вторые, и так далее.
    # Так как все источники для zip, это ссылки на один и тот же
    # итератор, при переходе от ссылки к ссылке курсор передвигается
    # всё дальше. Поэтому кортежи содержат последовательные элементы.
# END
