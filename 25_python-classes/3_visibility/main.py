#!/usr/bin/env python3

# https://ru.hexlet.io/courses/python-classes/lessons/visibility/exercise_unit
# https://ru.hexlet.io/code_reviews/1206847

# Python: Погружаясь в классы
# 3. Модификаторы доступа

'''
Реализуйте набор методов для работы с тегами:

add_tag(tag_name) – добавляет тег
remove_tag(tag_name) – удаляет тег
toggle_tag(tag_name) – ставит тег если его не было и убирает если он был

Эти методы должны обрабатывать свойство 'tag' (внутри строка)
cловаря attributes. В процессе реализации вам понадобится постоянно
преобразовывать строку тегов в список и обратно. Вынесите эту операцию в
отдельные функции и установите им правильный модификатор доступа.
'''

from HTMLDivElement import HTMLDivElement


def main():
    div = HTMLDivElement()
    div = HTMLDivElement({'tag': 'one two'})
    print(div.get_attribute('tag'))     ## 'one two'
    div.add_tag('small')
    print(div.get_attribute('tag'))     ## 'one two small'

    div.add_tag('small')
    print(div.get_attribute('tag'))     ## 'one two small'

    div.add_tag('one')
    print(div.get_attribute('tag'))     ## 'one two small'

    div.remove_tag('one')
    print(div.get_attribute('tag'))     ## 'two small'

    div.remove_tag('one')
    print(div.get_attribute('tag'))     ## 'two small'

    div.toggle_tag('zero')
    print(div.get_attribute('tag'))     ## 'two small zero'

    div.toggle_tag('one')
    print(div.get_attribute('tag'))     ## 'two small zero one'

    div.toggle_tag('zero')
    print(div.get_attribute('tag'))     ## 'two small one'
'''
'''

if __name__ == '__main__':
    main()


class Calculator:
    def calculate(self, x):
        return self.__helper(x) + 1

    def __helper(self, x):
        return x * x
