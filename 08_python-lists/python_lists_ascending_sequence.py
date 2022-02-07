# https://ru.hexlet.io/challenges/python_lists_ascending_sequence_exercise
# https://ru.hexlet.io/code_reviews/206985

# Python: Возрастающая последовательность
# ========================================

# Реализуйте функцию is_continuous_sequence, которая проверяет, является ли
# переданная последовательность целых чисел возрастающей непрерывно (не имеющей
# пропусков чисел). Например, последовательность [4, 5, 6, 7] — непрерывная,
# а [0, 1, 3] — нет. Последовательность может начинаться с любого числа.
# Главное условие — отсутствие пропусков чисел. Последовательность из одного
# числа не может считаться возрастающей.


def is_continuous_sequence(items):
    if len(items) < 2:
        return False
    for i in range(1, len(items)):
        if items[i] != items[i - 1] + 1:
            return False
    return True


assert is_continuous_sequence([10, 11, 12, 13]) == True
assert  is_continuous_sequence([-5, -4, -3]) == True
assert is_continuous_sequence([10, 11, 12, 14, 15]) == False
assert is_continuous_sequence([1, 2, 2, 3]) == False
assert is_continuous_sequence([7]) == False
assert is_continuous_sequence([]) == False


"""
def is_continuous_sequence(items):
    if len(items) < 2:
        return False
    return items[1:] == list(map(lambda x: x + 1, items[:-1]))
"""
