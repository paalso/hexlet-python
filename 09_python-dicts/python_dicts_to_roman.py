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
    roman_digits_table = {
        'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1
    }
    number = 0
    roman_digits = list(roman_number)
    roman_digits_copy = roman_digits.copy()

    for i in range(1, len(roman_digits_copy)):
        prev_roman_digit = roman_digits_copy[i - 1]
        prev_value = roman_digits_table[prev_roman_digit]
        current_roman_digit = roman_digits_copy[i]
        current_value = roman_digits_table[current_roman_digit]

        if prev_value < current_value:
            number += (current_value - prev_value)
            roman_digits.remove(prev_roman_digit)
            roman_digits.remove(current_roman_digit)

    for key, val in roman_digits_table.items():
        number += roman_digits.count(key) * val

    # Если переданное римское число не корректно,
    # то функция должна вернуть значение False
    if to_roman(number) != roman_number:
        return False

    return number


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
