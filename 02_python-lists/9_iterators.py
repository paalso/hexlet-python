# https://ru.hexlet.io/courses/python-lists/lessons/iterators/exercise_unit
# https://ru.hexlet.io/code_reviews/247662

# Python: Списки → Итераторы
# ===========================

# реализовать функцию find_second_index. В этом упражнении вам пригодится
# функция find_index, которую вы реализовали в прошлом упражнении. Напоминаю,
# эта функция возвращает индекс первого элемента последовательности, равного
# заданному значению. Функция find_second_index же должна возвращать индекс
# второго подходящего элемента в последовательности. Если подходящих элементов
# в последовательности меньше двух или же последовательность пуста, нужно всё
# так же возвращать None.


def find_index(value, items):
    for i, el in enumerate(items):
        if el == value:
            return i


def find_second_index(value, items):
    iter_ = iter(items)
    first = find_index(value, iter_)
    second = find_index(value, iter_)
    if not second is None:
        return first + second + 1


assert find_second_index('!', '') == None
assert find_second_index('!', '!') == None
assert find_second_index('n', 'clone')== None
assert find_second_index('n', 'banana') == 4
assert find_second_index('n', 'cannon') == 3
