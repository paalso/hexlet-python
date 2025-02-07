#!/usr/bin/env python3

# https://ru.hexlet.io/courses/python-polymorphism/lessons/state/exercise_unit
# https://ru.hexlet.io/code_reviews/1168131

# Python: Полиморфизм
# 16. Состояние(паттерн)

# Реализуйте класс TcpConnection в соответствии с примером

from tcp_connection import TcpConnection


def find_discrepancy(str1, str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return (i, str1[i], str2[i])


def main():
    connection = TcpConnection('11.22.33.11', 20)
    connection.connect()
    connection.disconnect()
    connection.disconnect()


if __name__ == '__main__':
    main()
