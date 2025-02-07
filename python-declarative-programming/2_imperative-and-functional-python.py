# https://ru.hexlet.io/courses/python-declarative-programming/lessons/imperative-and-functional-python/
# https://ru.hexlet.io/code_reviews/435425

# Функциональный и процедурный подходы в примерах
# ================================================

# Реализовать два решения одной и той же задачи — функциональное и процедурное.
# Для входного списка списков получить список нечётных по порядку списков
# (первый, третий и так далее), оставив в каждом только нечётные по порядку
# элементы. Например, для из списка [[1, 2, 3], [4, 5, 6], [7, 8, 9]] должен
# получиться список [[1, 3], [7, 9]].
# Функциональное решение должно вычислять новый список списков на основе
# оригинального. Оригинальный же список должен оставаться неизменным.
# Должна получиться функция odds_from_odds()

# Процедурное решение должно изменить список-аргумент по месту, а не возвращать
# его новую версию (возвращать вообще ничего не нужно!). Постарайтесь обойтись
# без создания вспомогательных структур в том числе и для обработки вложенных
# списков: процедурное решение должно быть эффективным с точки зрения
# использования памяти, ведь для этого мы такой код и пишем! У вас должна
# получиться процедура keep_odds_from_odds()

# Version 1


def odds_from_odds(list_of_lists):
    return list(map(lambda L: L[::2], list_of_lists))[::2]


L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert odds_from_odds(L) == [[1, 3], [7, 9]]
assert L == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert odds_from_odds([]) == []
assert odds_from_odds([[]]) == [[]]


def remove_even_positions(L):
    i = 0
    while True:
        i += 1
        if i >= len(L):
            break
        L.pop(i)


def keep_odds_from_odds(list_of_lists):
    remove_even_positions(list_of_lists)
    for L in list_of_lists:
        remove_even_positions(L)


L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert keep_odds_from_odds(L) is None
assert L== [[1, 3], [7, 9]]
keep_odds_from_odds(L)
assert L == [[1]]
keep_odds_from_odds(L)
assert L== [[1]]
assert keep_odds_from_odds([]) is None
assert keep_odds_from_odds([[]]) is None



"""
from operator import itemgetter

odds = itemgetter(slice(None, None, 2))
# ^ функция, которая вычисляет срез [::2] от аргумента


def odds_from_odds(list_of_lists):
    return list(map(odds, odds(list_of_lists)))


def keep_odd(some_list):
    del some_list[1::2]  # noqa: WPS420
    # Инструкция "del", это очень низкоуровневое действие и напрямую
    # использовать его мы не рекомендуем. Но другого способа очистить
    # срез "по месту", да ещё и за одно действие нет,
    # поэтому "del" здесь уместен.
    # Наш линтер за "del" ругает, поэтому пришлось отключить предупреждение!


def keep_odds_from_odds(list_of_lists):
    keep_odd(list_of_lists)  # отбрасываем чётные списки первого уровня
    for one_list in list_of_lists:  # затем в каждом из оставшихся списков...
        keep_odd(one_list)  # ...отбрасываем чётные элементы
"""

# Version 2
def extract_odds(items):
    return items[::2]


def remove_even(items):
    if len(items) < 2:
        return
    from_index = len(items) - 1 - len(items) % 2
    for i in range(from_index, 0, -2):
        items.pop(i)


def odds_from_odds(lists):
    return list(map(extract_odds, extract_odds(lists)))


def keep_odds_from_odds(lists):
    remove_even(lists)
    for items in lists:
        remove_even(items)

