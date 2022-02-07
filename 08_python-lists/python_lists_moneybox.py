# https://ru.hexlet.io/challenges/python_lists_moneybox_exercise
# https://ru.hexlet.io/code_reviews/243842

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


def visualize(coins, bar_char='₽'):
    nominals = sorted(set(coins))
    values = [coins.count(coin) for coin in nominals]
    plot_rows = []
    for i in range(max(values) + 1, 0, -1):
        row = []
        for _, val in enumerate(values):
            if i > val + 1:
                token = "  "
            elif i == val + 1:
                token = "{:<2}".format(val)
            else:
                token = bar_char * 2
            row.append(token)
        plot_rows.append(" ".join(row))
    plot_rows.append((3 * len(nominals) - 1) * "-")
    legend = " ".join(["{:<2}".format(nominal) for nominal in nominals])
    plot_rows.append(legend)
    return "\n".join(plot_rows)


print(visualize((10,1,1,1,1,1,20,20,20,2,2,2,2,3,3,3,3)))
# 6 5
# 5 ₽₽ 4  4
# 4 ₽₽ ₽₽ ₽₽    3
# 3 ₽₽ ₽₽ ₽₽    ₽₽
# 2 ₽₽ ₽₽ ₽₽ 1  ₽₽
# 1 ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
#   --------------
#   1  2  3  10 20

print()
print(visualize((10,1,1,1,1,1,20,20,20,2,2,2,2,3,3,3,3), bar_char='$'))

# 5
# $$ 4  4
# $$ $$ $$    3
# $$ $$ $$    $$
# $$ $$ $$ 1  $$
# $$ $$ $$ $$ $$
# --------------
# 1  2  3  10 20

