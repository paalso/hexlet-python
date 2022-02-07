# https://ru.hexlet.io/courses/python-dicts/lessons/modification-of-sets/exercise_unit
# Python: Словари и Множества → Изменение множеств

# Реализовать функцию all_unique, которая должна принимать итератор (в т.ч. и
# те, которые не перезапускаемые!) и возвращать True, если элементы в итераторе
# не повторяются (если элементов нет, то ничего не повторяется!).


# Функция toggle функция должна принимать флаг и множество в качестве аргументов.
# Если флаг уже присутствует в множестве, его нужно из множества убрать. Если же
# флаг отсутствует, то его нужно добавить. Таким образом функция будет
# переключать состояние флага. Множество нужно заменять "по месту", возвращать
# из функции ничего не нужно.

# Функция toggled функция работает похожим на toggle образом, но вместо
# изменения исходного множества возвращает новое — с уже переключенным флагом.


def toggle(flag, set_):
    set_.remove(flag) if flag in set_ else set_.add(flag)


def toggled(flag, set_):
    set_copy = set_.copy()
    toggle(flag, set_copy)
    return set_copy


READ_ONLY = 'read_only'
flags = set()
toggle(READ_ONLY, flags)
assert READ_ONLY in flags

toggle(READ_ONLY, flags)
assert not READ_ONLY in flags


READ_ONLY = 'read_only'
flags = set()
new_flags = toggled(READ_ONLY, flags)
assert not READ_ONLY in flags
assert READ_ONLY in new_flags
