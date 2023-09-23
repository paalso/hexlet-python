from strategies.easy import Easy
from strategies.normal import Normal


class TicTacToe():
    player_symbol = 'X'
    ai_symbol = 'O'
    empty_symbol = '.'

    strategies = {
        'easy': Easy,
        'normal': Normal,
    }

    def __init__(self, level='easy'):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.size = len(self.field)
        self.level = self.__class__.strategies[level]()

    def __str__(self):
        return '\n'.join(' '.join(map(self.__represent_cell, line))
                         for line in self.field)

    def print_field(self):
        print(str(self))

    def go(self, row=None, col=None):
        if row is None and col is None:
            row, col = self.level.go(self.field, self.__class__.ai_symbol)
        else:
            self.field[row][col] = self.__class__.player_symbol
        return self.__check_victory(row, col)

    def __check_victory(self, row, col):
        return self.__check_victory_in_row(row) or \
               self.__check_victory_in_column(col) or \
               self.__check_victory_in_diagonals()

    def __check_victory_in_row(self, row):
        if not (first_in_row := self.field[row][0]):
            return False
        return all(map(lambda e: first_in_row == e, self.field[row]))

    def __check_victory_in_column(self, col):
        if not (first_in_col := self.field[0][col]):
            return False
        return all(map(lambda e: first_in_col == e,
                       (self.field[row][col]
                        for row in range(self.size))))

    def __check_victory_in_diagonals(self):
        if (first_in_diag := self.field[0][0]) and \
            all(map(lambda e: first_in_diag == e,
                    (self.field[row][row]
                     for row in range(self.size)))):
            return True
        if (first_in_diag := self.field[0][self.size - 1]) and \
            all(map(lambda e: first_in_diag == e,
                    (self.field[row][self.size - 1 - row]
                     for row in range(self.size)))):
            return True
        return False

    def __represent_cell(self, cell):
        return cell or self.__class__.empty_symbol
