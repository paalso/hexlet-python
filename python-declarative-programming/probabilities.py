# https://ru.hexlet.io/challenges/python_declarative_programming_probabilities_exercise/instance
# https://ru.hexlet.io/code_reviews/1108504

# Функции-генераторы
# ====================

# Реализовать функцию calculate_probabilities(), которая принимает на вход
# историю подбрасывания кубика в виде списка и возвращает словарь. Ключом
# этого словаря служит число из списка, а значением – ещё один словарь, в
# котором ключи – это числа, выпавшие сразу после первоначального числа,
# а значения – вероятность их выпадения.

from collections import Counter


def get_probabilities_for_key(data, key):
    after_key_values = list(val for e, val in zip(data, data[1:]) if e == key)
    key_probabilities = Counter(after_key_values)

    if key_probabilities:
        normalizing_factor = 1 / len(after_key_values)
        for key in key_probabilities.keys():
            key_probabilities[key] *= normalizing_factor

    return dict(key_probabilities)


def calculate_probabilities(data):
    return {key: get_probabilities_for_key(data, key) for key in set(data)}


# Hexlet version
# def calc_probability(nums, num):
#     filtered = [nums[i] for i in range(1, len(nums)) if nums[i - 1] == num]
#     probability = {n: filtered.count(n) / len(filtered) for n in filtered}
#     return probability


# def calculate_probabilities(dices):
#     return dict((dice, calc_probability(dices, dice)) for dice in dices)