# https://ru.hexlet.io/challenges/python_functions_find_nearest
# https://ru.hexlet.io/code_reviews/257709

# Python: Функции → Поиск ближайшего соседа

# Реализуйте функцию find_index_of_nearest, которая принимает на вход список
# чисел и искомое число. Задача функции — найти в списке ближайшее число к
# искомому и вернуть его индекс.
# Если в списке содержится несколько чисел, одновременно являющихся ближайшими
# к искомому числу, то возвращается наименьший из индексов ближайших чисел.


def find_index_of_nearest(number, items):
    if items:
        return min(range(len(items)), key=lambda i: abs(items[i] - number))


assert find_index_of_nearest(2, []) is None
assert find_index_of_nearest(0, [15, 10, 3, 4]) == 2
assert find_index_of_nearest(4, [7, 5, 3, 2]) == 1
assert find_index_of_nearest(4, [7, 5, 4, 4, 3]) == 2


'''
# BEGIN
def find_index_of_nearest(number, source):
    if source:
        diff = list(map(lambda x: abs(x - number), source))
        return diff.index(min(diff))
# END
'''
