from strategies.easy import Easy
from strategies.normal import Normal


class TicTacToe():
    # Player plays with crosses, AI plays with noughts
    HUMAN_MARK = 'X'
    AI_MARK = 'O'
    LEVELS = {
        'easy': Easy,
        'normal': Normal,
    }

    def __init__(self, level='easy'):
        self.field = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

        strategy_cls = self.LEVELS.get(level)
        self.strategy = strategy_cls()

    def go(self, *coords):
        if coords:
            return self._go_human(*coords)
        else:
            return self._go_ai()

    def _go_human(self, *coords):
        x, y = coords
        self.field[x][y] = self.HUMAN_MARK
        return self._check_winning_move(x, y)

    def _go_ai(self):
        free_space = self.strategy.go(self.field)
        x, y = free_space
        self.field[x][y] = self.AI_MARK
        return self._check_winning_move(x, y)

    def _check_winning_move(self, x, y):
        mark = self.field[x][y]
        return self._check_horizontal_win(mark, x) or \
               self._check_vertical_win(mark, y) or \
               self._check_diagonal_win(mark)

    def _check_horizontal_win(self, mark, row):
        return all(self.field[row][y] == mark for y in range(3))

    def _check_vertical_win(self, mark, col):
        return all(self.field[x][col] == mark for x in range(3))

    def _check_diagonal_win(self, mark):
        if all(self.field[i][i] == mark for i in range(3)):
            return True
        if all(self.field[i][2 - i] == mark for i in range(3)):
            return True
        return False

    def print_field(self):
        def render_cell(cell):
            return cell if cell is not None else ' '

        for i, row in enumerate(self.field):
            print(' | '.join(render_cell(cell) for cell in row))
            if i < 2:
                print('-' * 9)

        print()
