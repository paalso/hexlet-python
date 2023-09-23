class Easy():
    def go(self, field, symbol):
        for row in range(len(field)):
            for col in range(len(field[0])):
                if field[row][col] is None:
                    field[row][col] = symbol
                    return row, col
