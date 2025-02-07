#!/usr/bin/env python3

# https://ru.hexlet.io/courses/python-polymorphism/lessons/decorator/exercise_unit
# https://ru.hexlet.io/code_reviews/1162552

# Python: Полиморфизм
# 13. Декоратор (Паттерн)

# Реализуйте декоратор-логгер CalcLogger() для класса Calculator() из модуля.
# Декоратор оборачивает методы sum(), sub(), mul() и печатает строки при
# использовании этих методов:

from calculator import Calculator
from calc_logger import CalcLogger
from calc_logger_pro import CalcLoggerPro


def main():
    calc = Calculator(5)
    calc = CalcLogger(calc)
    print(calc.sum(5).mul(5).sub(10).result())
    print(calc.result())
    assert calc.result() == 40

    calc = Calculator(5)
    calc = CalcLoggerPro(calc)
    print(calc.sum(5).mul(5).sub(10).result())
    print(calc.result())
    assert calc.result() == 40


if __name__ == '__main__':
    main()
