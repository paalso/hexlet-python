#!/usr/bin/env python3

# https://ru.hexlet.io/courses/python-classes/lessons/template-method/exercise_unit
# https://ru.hexlet.io/code_reviews/1210439

# Python: Погружаясь в классы
# 5. Шаблонный метод

'''
Реализуйте класс HTMLPairElement (наследуется от HTMLElement),
который отвечает за генерацию представления парных элементов и
работу с телом. Реализуйте следующий интерфейс:

метод __str__() - возвращает строковое представление элемента
метод get_text_content() - возвращает тело элемента
метод set_text_content(body) - устанавливает тело элемента
'''

from HTMLDivElement import HTMLDivElement


def main():
    div = HTMLDivElement({'name':'div', 'data-toggle':'true'})
    print(div.get_text_content())
    div.set_text_content('Body Text')
    print(div.get_text_content())  # Body Text
    print(str(div))


if __name__ == '__main__':
    main()
