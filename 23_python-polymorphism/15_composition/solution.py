#!/usr/bin/env python3

# https://ru.hexlet.io/courses/python-polymorphism/lessons/composition/exercise_unit
# https://ru.hexlet.io/code_reviews/1165340

# Python: Полиморфизм
# 15. Объектная композиция

'''
Адаптер – популярный шаблон проектирования. Он используется тогда, когда нужно
использовать код, не поддерживающий необходимый интерфейс. В такой ситуации
создается "обертка" над необходимым кодом, которая поддерживает нужный
интерфейс. Это очень похоже на адаптеры электронных устройств в реальной
жизни.

В текущем задании, есть код, отвечающий за генерацию паролей. Он находится в
классе PasswordBuilder. Для генерации паролей, этот класс использует внешнюю
библиотеку.

Реализуйте класс PasswordGeneratorAdapter, который представляет собой адаптер
к библиотеке passgen.py.
'''

from password_builder import PasswordBuilder
from passgen_adapter import PasswordGeneratorAdapter


def main():
    builder = PasswordBuilder(PasswordGeneratorAdapter())

    # Первый параметр длина пароля
    # Второй, набор опций
    password_info = builder.build_password(10, ['uppercase', 'digits'])
    print(password_info)
    # {
    #    password: 'zUqlhoGm3G',
    #    digest: '080c729e3389eb8dd470e97b6c7327c6fc35aa85',
    # }

    password_info2 = builder.build_password(10, [])
    print(password_info2)
    # {
    #    password: 'aslgyesjdp',
    #    digest: '8ebc8fe30d3c92d8b58aadc520a29c06f113e937',
    # }


if __name__ == '__main__':
    main()
