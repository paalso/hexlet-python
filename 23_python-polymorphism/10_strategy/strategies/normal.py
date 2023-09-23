class Normal():
    def go(self, field, symbol):
        for row in range(len(field) - 1, -1, -1):
            for col in range(len(field[0])):
                if field[row][col] is None:
                    field[row][col] = symbol
                    return row, col
