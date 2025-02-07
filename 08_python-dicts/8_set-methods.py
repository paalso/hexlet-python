# https://ru.hexlet.io/courses/python-dicts/lessons/set-methods/exercise_unit
# Python: Словари и Множества →  Методы объектов множеств

# Реализовать функция apply_diff. Эта функция принимает два аргумента, первым
# из которых выступает множество, которое нужно будет изменять "по месту"
# (возвращать ничего не нужно). Вторым аргументом функция принимает словарь,
# который может содержать ключи 'add' и 'remove' с множествами в качестве
# значений. Значения по ключу 'add' нужно добавить в изменяемое множество,
# а значения по ключу 'remove' — убрать из множества. Прочие ключи в переданном
# словаре значения не имеют и обрабатываться не должны.


def apply_diff(set_, diff_dict):
    if "add" in diff_dict:
        set_.update(diff_dict["add"])
    if "remove" in diff_dict:
        set_.difference_update(diff_dict["remove"])


target = {'a', 'b'}
diff = {'add': {'c'}, 'remove': {'a'}}
apply_diff(target, diff)
assert target == {'c', 'b'}


"""
def apply_diff(set_for_update, diff):
    set_for_update.update(diff.get('add', {}))
    set_for_update.difference_update(diff.get('remove', {}))
"""
