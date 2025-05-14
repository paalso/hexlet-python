class Easy():
    def go(self, field):
        for x in range(3):
            for y in range(3):
                if field[x][y] is None:
                    return x, y
