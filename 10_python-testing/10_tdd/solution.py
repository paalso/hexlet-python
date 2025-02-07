#!/usr/bin/env python
# -*- coding: utf-8 -*- 


# https://ru.hexlet.io/courses/python-testing/lessons/tdd/exercise_unit
# https://ru.hexlet.io/code_reviews/477292

# Разработка через тестирование (TDD)
# ====================================

"""
Напишите тесты для функции fill(coll, value, begin, end),
которая заполняет элементы списка переданным значением,
начиная со старта и заканчивая (но не включая) конечной позицией.
Функция меняет исходный список!

Функция принимает следующие аргументы:
coll – список, элементы которого будут заполнены
value – значение, которым будут заполнены элементы списка
begin – стартовая позиция, по умолчанию равна нулю
end – конечная позиция, по умолчанию равна длинне списка"""


def fill(coll, value, begin=0, end=None):
    coll_size = len(coll)
    begin = max(0, begin)
    end = min(coll_size, end) if end else coll_size

    coll[begin:end] = [value] * (end - begin)


# Плохое кмк решение, и неправильное
# Author's solution
# def fill(coll, value, begin=0, end=None):
#     chunk = [value for _ in coll[begin:end]]
#     coll[begin:end] = chunk

def main():
    L = [1,2,3,4]
    fill(L, '%', -1, 10)
    print(L)

if __name__ == "__main__":
    main()
