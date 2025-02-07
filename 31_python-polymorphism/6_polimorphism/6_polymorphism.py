# https://ru.hexlet.io/courses/python-polymorphism/lessons/polymorphism/exercise_unit


# Python: Полиморфизм
# 4. Диспетчеризация по имени файла

'''
Реализуйте класс InMemoryKV, который представляет собой in-memory key-value
хранилище. Данные внутри него хранятся в обычном словаре. Интерфейс этого
класса совпадает с FileKV за исключением __init__.py. Инициализатор InMemoryKV
принимает на вход словарь, который становится начальным значением базы данных.

Реализуйте и функцию swap_key_value(), которая принимает на вход объект базы
данных и меняет в нём ключи и значения местами.

swap_key_value() — полиморфная функция, она может работать с любой реализацией
key-value, имеющей такой же интерфейс.
'''
import copy
from in_memory_kv import InMemoryKV


def swapped_dict(dict_: dict) -> dict:
    return dict(map(lambda p: (p[1], p[0]), dict_.items()))


def swap_key_value(kv_storage):
    swapped_items = map(lambda p: (p[1], p[0]), kv_storage.to_dict().items())
    kv_storage.clear_()
    for k, v in swapped_items:
        kv_storage.set_(k, v)


def test_in_memory_kv():
    data = {'key': 10}
    map = InMemoryKV(data)

    assert map.get_('key2') is None
    assert map.get_('key2', 'default') == 'default'
    assert map.get_('key') == 10
    assert map.get_('key', 'default') == 10

    map.set_('key2', 'value2')
    map.set_('key', 'value')

    assert map.get_('key2', 'default') == 'value2'
    assert map.get_('key2') == 'value2'
    assert map.get_('key') == 'value'

    map.unset_('key')

    assert map.get_('key') is None
    assert map.to_dict() == {'key2': 'value2'}


def test_get_default_value():
    data = {'key': 10}
    map = InMemoryKV(data)

    assert map.get_('key2', 'default') == 'default'

    map.set_('key2', False)
    assert map.get_('key2', 'default') is False


def test_must_be_immutable():
    data = {'key': 10}
    data_copy = copy.deepcopy(data)
    map = InMemoryKV(data)

    data['key2'] = 'value2'
    assert map.to_dict() == data_copy

    map2 = map.to_dict()
    map2['key2'] = 'value2'
    assert map.to_dict() == data_copy


def test_deep_immutable():
    data = {'key1': 'value1', 'key2': {'key3': 'value2'}}
    data_copy = copy.deepcopy(data)
    map = InMemoryKV(data)

    map2 = map.to_dict()
    map2['key2']['key3'] = 'another value'

    assert map.to_dict() == data_copy


def test_swap_key_value():
    map = InMemoryKV({'key': 10})
    map.set_('key2', 'value2')
    swap_key_value(map)

    assert map.get_('key') is None
    assert map.get_(10) == 'key'
    assert map.get_('value2') == 'key2'


def test_swap_key_value2():
    map = InMemoryKV({'foo': 'bar', 'bar': 'zoo'})

    swap_key_value(map)
    print(map.to_dict())
    assert map.to_dict() == {'bar': 'foo', 'zoo': 'bar'}


# map = InMemoryKV({'key': 10})
# map.set_('key2', 'value2')
# swap_key_value(map)

# print(f'key : {map.get_("key")}')       # None
# print(f'10  : {map.get_(10)}')          # 'key'
# print(f'key2: {map.get_("key2")}')          # 'key'
# print("map.unset('key2')")
# map.unset('key2')
# print(f'key2: {map.get("key2")}')          # 'key'

# print(map.get('value2'))    # 'key2'
# print(map.to_dict())
# swap_key_value(map)
# print(map.to_dict())

test_in_memory_kv()
test_get_default_value()
test_must_be_immutable()
test_deep_immutable()
test_swap_key_value()
test_swap_key_value2()
