# https://ru.hexlet.io/challenges/python_dicts_to_roman
# https://ru.hexlet.io/code_reviews/254097

# Python: Римские цифры
# ======================

# Для записи цифр римляне использовали буквы латинского алфафита:
# I, V, X, L, C, D, M. Например:
#
# Реализуйте функцию to_roman, которая переводит арабские числа в римские.
# Функция принимает на вход целое число из диапазона от 1 до 3000, а возвращает
# строку с римским представлением этого числа.
#
# Реализуйте функцию to_arabic, которая переводит число в римской записи в
# число, записанное арабскими цифрами.


def to_roman(number):
    roman_digits_table = {
        1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L',
        40:'XL', 10:'X', 9:'IX', 5:'V', 4: 'IV', 1:'I'
    }
    roman_digits = []
    for divisor in sorted(roman_digits_table.keys(), reverse=True):
        digit = roman_digits_table[divisor]
        digits_qty, number = divmod(number, divisor)
        roman_digits.append(digits_qty * digit)
    return ''.join(roman_digits)


def to_arabic(roman_number):
    if not roman_number:
        return 0

    roman_to_arabic_map = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1,
    }

    def reversed_order_factor(roman_1, roman_2):
        if roman_to_arabic_map[roman_1] < roman_to_arabic_map[roman_2]:
            return -1
        return 1

    arabic_number = 0
    for i in range(len(roman_number) - 1):
        current_roman_digit, next_roman_digit = roman_number[i:i + 2]
        arabic_number += \
            reversed_order_factor(current_roman_digit, next_roman_digit) * \
            roman_to_arabic_map[current_roman_digit]
    arabic_number += roman_to_arabic_map[roman_number[-1]]
    if to_roman(arabic_number) == roman_number:
        return arabic_number
    return False


assert to_arabic('I') == 1
assert to_arabic('II') == 2
assert to_arabic('IV') == 4
assert to_arabic('V') == 5
assert to_arabic('VI') == 6
assert to_arabic('XXVII') == 27
assert to_arabic('XLVIII') == 48
assert to_arabic('LIX') == 59
assert to_arabic('XCIII') == 93
assert to_arabic('CXLI') == 141
assert to_arabic('CLXIII') == 163
assert to_arabic('CDII') == 402
assert to_arabic('DLXXV') == 575
assert to_arabic('CMXI') == 911
assert to_arabic('MXXIV') == 1024
assert to_arabic('MMXX') == 2020
assert to_arabic('MMM') == 3000
assert to_arabic('IIII') is False
