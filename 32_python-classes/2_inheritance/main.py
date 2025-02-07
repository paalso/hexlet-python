#!/usr/bin/env python3

# https://ru.hexlet.io/courses/python-classes/lessons/inheritance/exercise_unit

# Python: Погружаясь в классы
# 2. Наследование

'''
Реализуйте класс HTMLHrElement (наследуется от HTMLElement), который отвечает
за представление тега <hr>. Внутри класса определите функцию __str__, которая
возвращает текстовое представление тега.

Реализуйте метод _stringify_attributes(), который формирует строчку для
аттрибутов. Используйте этот метод в наследнике для формирования тега.
'''

from HTMLAnchorElement import HTMLAnchorElement
from HTMLHrElement import HTMLHrElement


def main():
    hr = HTMLHrElement()
    print(hr) #=> <hr>

    hr = HTMLHrElement({'class':'w-75', 'id':'wop'})
    print(hr) #=> '<hr class="w-75" id="wop">'


if __name__ == '__main__':
    main()
