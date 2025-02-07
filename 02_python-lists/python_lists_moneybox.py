# https://ru.hexlet.io/challenges/python_lists_moneybox_exercise
# https://ru.hexlet.io/code_reviews/243874

# Python: Копилка
# ================

# Реализуйте функцию visualize, которая подсчитывает сколько монет каждого
# номинала есть в копилке и показывает результат в виде графика. Каждый столбец
# графика — стопка монет опредлённого номинала.

# Для простоты условимся, что монеты в копилке всегда есть, и их количество не
# ограничено, а номинал может быть любым.
#
# Функция принимает на вход список или кортеж с числами и возвращает график
# в виде строки. Необязательный аргумент bar_char определяет символ, с помощью
# которого рисуется график. Значение по умолчанию — знак рубля (₽).

from collections import Counter


def bar_token(histogram, x, y, bar_char):
    max_x_value = histogram[x]
    if y > max_x_value + 1:
        return '  '
    if y == max_x_value + 1:
        return str(max_x_value).ljust(2, ' ')
    if 0 < y < max_x_value + 1:
        return bar_char * 2
    if y == 0:
        return '--'
    if y == -1:
        return str(x).ljust(2, ' ')


def bar_row_tokens_separator(y):
    return '-' if y == 0 else ' '


def visualize(data, bar_char="₽"):
    histogram = Counter(data)
    max_value = max(histogram.values())
    ordered_histogram_keys = sorted(histogram.keys())
    bar_rows = []

    bar_rows = (
        bar_row_tokens_separator(y).join(
            bar_token(histogram, x, y, bar_char) for x in ordered_histogram_keys
        )
        for y in range(max_value + 1, -2, -1)
    )

    return "\n".join(bar_rows)


print(visualize((10, 1, 1, 1, 1, 1, 20, 20, 20, 2, 2, 2, 2, 3, 3, 3, 3)))
# 6 5
# 5 ₽₽ 4  4
# 4 ₽₽ ₽₽ ₽₽    3
# 3 ₽₽ ₽₽ ₽₽    ₽₽
# 2 ₽₽ ₽₽ ₽₽ 1  ₽₽
# 1 ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
#   --------------
#   1  2  3  10 20

print()
print(visualize((10, 1, 1, 1, 1, 1, 20, 20, 20, 2, 2, 2, 2, 3, 3, 3, 3),
                bar_char="$"))


# 5
# $$ 4  4
# $$ $$ $$    3
# $$ $$ $$    $$
# $$ $$ $$ 1  $$
# $$ $$ $$ $$ $$
# --------------
# 1  2  3  10 20
