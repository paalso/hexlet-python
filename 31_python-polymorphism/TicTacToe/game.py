#!/usr/bin/env python3

from tic_tac_toe import TicTacToe

def main():
    game = TicTacToe('normal')
    game.go(1, 1)
    game.print_field()
    game.go()
    game.print_field()
    game.go(0, 1)
    game.print_field()
    game.go()
    game.print_field()
    is_winner = game.go(2, 1)
    game.print_field()
    print(is_winner)


if __name__ == '__main__':
    main()
