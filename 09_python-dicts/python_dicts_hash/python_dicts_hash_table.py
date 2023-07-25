# https://ru.hexlet.io/challenges/python_dicts_hash_table_exercise/
# https://ru.hexlet.io/code_reviews/1091135

# Python: Ассоциативный массив 
# =========================

# Реализовать словарь:
# set_(map, key, value) — устанавливает в массив значение по ключу. Работает
# и для создания, и для изменения. Функция возвращает True, если удалось
# установить значение. При возникновении коллизии функция никак не меняет
# массив и возвращает False
# get_(map, key, default = None) — возвращает значение указанного ключа.
# Параметр default — значение, которое функция возвращает, если в словаре нет
# ключа (по умолчанию равно None). При возникновении коллизии функция также
# возвращает значение по умолчанию

import zlib
from map import make


def get_hash(value):
    MAX_SIZE = 19
    return zlib.crc32(value) % MAX_SIZE


def has_collision(map, key):
    id_ = get_hash(key)
    current_item = map[id_]
    if current_item is None:
        return False

    current_key, _ = current_item
    return key != current_key


def get_(map, key, default=None):
    id_ = get_hash(key)
    current_item = map[id_]

    if not current_item or has_collision(map, key):
        return default

    _, current_value = current_item
    return current_value


def set_(map, key, value):
    id_ = get_hash(key)

    if has_collision(map, key):
        return False

    map[id_] = [key, value]
    return True


map = make()
assert get_(map, b'key') is None
assert get_(map, b'key', b'value') == b'value'

set_(map, b'key2', b'value2')
assert get_(map, b'key2') == b'value2'
assert get_(map, b'None') is None

set_(map, b'key2', b'another value')
assert get_(map, b'key2') == b'another value'


map = make()
assert set_(map, b'aaaaa0.462031558722291', b'vvv') is True
assert set_(map, b'aaaaa0.0585754039730588', b'boom!') is False
assert get_(map, b'aaaaa0.462031558722291') == b'vvv'
assert get_(map, b'aaaaa0.0585754039730588') is None

set_(map, b'aaaaa0.462031558722291', b'wop')
assert get_(map, b'aaaaa0.462031558722291') == b'wop'
