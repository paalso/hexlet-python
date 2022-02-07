# https://ru.hexlet.io/challenges/python_functions_rgb_hex_conversion
# https://ru.hexlet.io/code_reviews/259157

# Python: Функции → Конвертер цветов

# При работе с цветами часто нужно получить отдельные значения красного,
# зеленого и синего (RGB) компонентов цвета в десятичной системе исчисления и
# наоборот. Реализуйте функцию rgb2hex, которая конвертирует цвета в
# соответвующее представление.
# Функция rgb2hex принимает 3 параметра (цветые компоненты) и возвращает
# строку. Функция должна работать как с позиционными,
# так и с именованными аргументами.


def hex2rgb(hex_num :str):
    import textwrap
    return dict(
            zip(('r', 'g', 'b'),
            map(lambda e: int(e, 16), textwrap.wrap(hex_num[1:], 2))))


def rgb2hex(r=None, g=None, b=None):
    def int_to_hex_str(n):
        return hex(n)[2:].rjust(2, '0')

    return "#{}".format("".join(map(int_to_hex_str, (r, g, b))))


assert rgb2hex(36, 171, 0) == '#24ab00'
assert rgb2hex(r=36, g=171, b=0) == '#24ab00'

assert hex2rgb('#24ab00') == {'r': 36, 'g': 171, 'b': 0}



'''
def hex2rgb(color):
    r, g, b = map(lambda channel: int(channel, 16), wrap(color[1:], 2))
    return {'r': r, 'g': g, 'b': b}


def convert(channel):
    return hex(channel)[2:].rjust(2, '0')


def rgb2hex(r=None, g=None, b=None):
    return '#{}{}{}'.format(*map(convert, [r, g, b]))


# Альтернативное решение с использованием возможностей .format
# https://docs.python.org/3.4/library/string.html#format-specification-mini-language
# def rgb2hex(r=None, g=None, b=None):
#     return '#{:02x}{:02x}{:02x}'.format(r, g, b)
# END
'''
