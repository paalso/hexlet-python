# https://ru.hexlet.io/courses/python-lists/lessons/for-loop/exercise_unit

# Python: Списки → Цикл for
# ==========================

# Реализовать классический цикл поиска. Функция find_index, которую вам
# предстоит написать, должна принимать значение и нечто, по чему можно
# итерироваться — строку, список, кортеж. В ответ функция должна вернуть индекс
# первого элемента итерируемой последовательности, равного заданному значению.
# Если же значение в последовательности не встречается или же последовательность
# окажется пустой, функция должна вернуть None.


def find_index(value, items):
    for i, el in enumerate(items):
        if el == value:
            return i


assert find_index('t', 'cat') == 2
assert find_index(5, [1, 2, 3, 4, 5, 6, 7]) == 4
assert find_index(42, []) is None
assert find_index('!', 'abc') is None
