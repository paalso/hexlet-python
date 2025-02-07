# https://ru.hexlet.io/challenges/python_functions_same_parity/instance

# Python: Функции → IP конвертер

# Реализуйте функции ip2int() и int2ip(), которые преобразовывают
# представление IP-адреса из десятичного формата с точками в 32-битное
# число в десятичной форме и обратно.

# Функция ip2int принимает на вход строку и должна возвращать число.
# А функция int2ip наоборот: принимает на вход число, а возвращает строку

from operator import mul


def ip2int(ip):
    ip_tokens = map(int, ip.split('.'))
    hex_mask = (256 ** 3, 256 ** 2, 256, 1)
    return sum(map(mul, ip_tokens, hex_mask))


def int2ip(number):
    ip_tokens = []
    for i in range(4):
        number, ip_token = divmod(number, 256)
        ip_tokens.append(ip_token)
    return '.'.join(map(str, reversed(ip_tokens)))


assert ip2int('128.32.10.1') == 2149583361
assert ip2int('0.0.0.0') == 0
assert ip2int('255.255.255.255') == 4294967295

assert int2ip(2149583361) == '128.32.10.1'
assert int2ip(0) == '0.0.0.0'
assert int2ip(4294967295) == '255.255.255.255'
