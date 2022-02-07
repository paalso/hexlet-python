# https://ru.hexlet.io/challenges/python_lists_hamming_weight_exercise

# Python: Вес Хэмминга
# =====================

# Вес Хэмминга это количество единиц в двоичном представлении числа.
# Реализуйте функцию hamming_weight, которая считает вес Хэмминга.



def hamming_weight(n):
    return bin(n).count('1')


assert hamming_weight(0) == 0
assert hamming_weight(4) == 1
assert hamming_weight(101) == 4
