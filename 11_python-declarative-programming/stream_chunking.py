# https://ru.hexlet.io/challenges/python_declarative_programming_intersperse_exercise
# 

# Чанкование потока
# ==================

# Реализовать функцию ichunks(), которая должна принимать в качестве
# аргументов размер кусочка (положительное целое число) и источник данных
# (итератор). Вернуть функция должна итератор списков заданной длины,
# содержащих элементы из источника данных.

from itertools import count, islice


def ichunks(chunk_size, itarable):
    splitted_itarable = (itarable[i::chunk_size] for i in range(chunk_size))
    return map(list, zip(*splitted_itarable))


assert list(ichunks(1, [])) == []
assert list(ichunks(2, [42])) == []
assert list(ichunks(1, [100, 200])) == [[100], [200]]

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
