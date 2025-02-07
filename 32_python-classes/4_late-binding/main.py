#!/usr/bin/env python3

# https://ru.hexlet.io/courses/python-classes/lessons/late-binding/exercise_unit
# https://ru.hexlet.io/code_reviews/1209298

# Python: Погружаясь в классы
# 4. Позднее связывание
'''
Реализуйте метод is_instance_of(class_name), который проверяет что объект
принадлежит одному из классов в цепочке наследования.
'''

from ChildOfChild import ChildOfChild


def main():
    obj = ChildOfChild()

    print(obj.is_instance_of('Base')) ##  True
    print(obj.is_instance_of('Child'))  ## True
    print(obj.is_instance_of('ChildOfChild'))  ## True
    print(obj.is_instance_of('SomeClass'))  ## False


if __name__ == '__main__':
    main()
