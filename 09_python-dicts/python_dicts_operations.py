# https://ru.hexlet.io/challenges/python_dicts_operations
# https://ru.hexlet.io/code_reviews/342846

# Python: Вычислитель различий
# =============================

# Реализуйте функцию gen_diff, которая сравнивает два словаря и возвращает
# результат сравнения в виде словаря. Ключами результирующего словаря будут
# все ключи из двух входящих, а значением строка с описанием отличий:
# added, deleted, changed или unchanged.

# Возможные значения:
# added — ключ отсутствовал в первом словаре, но был добавлен во второй
# deleted — ключ был в первом словаре, но отсутствует во втором
# changed — ключ присутствовал и в первом и во втором словаре, но значения отличаются
# unchanged — ключ присутствовал и в первом и во втором словаре с одинаковыми значениями


def genDiff(oldDict, newDict):
    diffDict = dict()

    # это излишне, ведь достаточно проверить key in oldDict, например
    oldKeys, newKeys = oldDict.keys(), newDict.keys()
    for key in oldKeys | newKeys:
        if key not in oldKeys:
            diffDict[key] = "added"
        elif key not in newKeys:
            diffDict[key] = "deleted"
        elif newDict[key] != oldDict[key]:
            diffDict[key] = "changed"
        else:
            diffDict[key] = "unchanged"
    return diffDict


print(genDiff(
    {"one": "eon", "two": "two", "four": True},
    {"two": "own", "zero": 4, "four": True},
))
# {"one": "deleted", "two": "changed", "four": "unchanged", "zero": "added"}

print(genDiff(
    {'host': 'hexlet.io', 'timeout': 50, 'proxy': '123.234.53.22', 'follow': False},
    {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'},
))

print(
"""
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
)