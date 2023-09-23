#!/usr/bin/env python3

# https://ru.hexlet.io/courses/python-polymorphism/lessons/strategy/exercise_unit
# https://ru.hexlet.io/code_reviews/1151513

# Python: Полиморфизм
# 10. Стратегия (Паттерн)

'''
Реализуйте класс TicTacToe, который представляет собой игру крестики-нолики. 

Реализуйте стратегию, которая пытается заполнить поля, пробегаясь построчно
слева направо и сверху вниз (начиная с левого верхнего угла). Как только она
встречает свободное поле, то вставляет туда значение.

Реализуйте стратегию, которая пытается заполнить поля, пробегаясь построчно
слева направо и снизу вверх (начиная с левого нижнего угла). Как только она
встречает свободное поле, то вставляет туда значение.
'''

from tic_tac_toe import TicTacToe


def test_easy_game1():
    game = TicTacToe()
    game.go(1, 1)
    game.go()
    game.go(0, 1)
    game.go()
    is_winner = game.go(2, 1)
    assert is_winner


def test_easy_game2():
    game = TicTacToe()
    game.go(1, 1)
    game.go()
    game.go(1, 2)
    assert not game.go()
    assert not game.go(2, 2)
    is_winner = game.go()
    assert is_winner


def test_easy_game3():
    game = TicTacToe()
    game.go(0, 0)
    game.go()
    assert not game.go(1, 1)
    assert not game.go()
    is_winner = game.go(2, 2)
    assert is_winner


def test_normal_game1():
    game = TicTacToe('normal')
    game.go(0, 2)
    game.go()
    game.go(0, 1)
    assert not game.go()
    assert not game.go(1, 2)
    is_winner = game.go()
    assert is_winner


def test_normal_game2():
    game = TicTacToe('normal')
    game.go()
    game.go(2, 1)
    game.go()
    game.go(1, 0)
    assert not game.go()
    assert not game.go(1, 2)
    is_winner = game.go()
    assert is_winner


def test_normal_game3():
    game = TicTacToe('normal')
    game.go(2, 2)
    game.go()
    assert not game.go(1, 1)
    assert not game.go()
    is_winner = game.go(0, 0)
    assert is_winner


def main():
    test_easy_game1()
    test_easy_game2()
    test_easy_game3()
    test_normal_game1()
    test_normal_game2()
    test_normal_game3()


if __name__ == '__main__':
    main()
