# https://ru.hexlet.io - /courses/python-dicts/lessons/operations-on-sets/exercise_unit
# Python: Словари и Множества →  Операции над множествами

# Реализовать функцию diff_keys, которая должна принимать два словаря-аргумента
# — "старый" и "новый" — и возвращать словарь с результатами анализа.
# Результирующий словарь должен содержать строго три ниже перечисленных ключа:

# 'kept' — множество ключей, которые присутствовали в старом словаре и остались
# в новом;
# 'added' — множество ключей, которые отсутствовали в старом словаре,
# но появились в новом;
# 'removed' — множество ключей, которые присутствовали в старом словаре,
# но в новый не вошли.


def diff_keys(old_dict, new_dict):
    old_keys = old_dict.keys()
    new_keys = new_dict.keys()

    return {
        "added": new_keys - old_keys,
        "removed": old_keys - new_keys,
        "kept": old_keys & new_keys,
    }


assert diff_keys({'name': 'Bob', 'age': 42}, {}) == {'kept': set(), 'added': set(), 'removed': {'name', 'age'}}
assert diff_keys({'a': 2}, {'a': 1}) == {'kept': {'a'}, 'added': set(), 'removed': set()}
assert diff_keys({'a': 2}, {'a': 1}) == {'kept': {'a'}, 'added': set(), 'removed': set()}
