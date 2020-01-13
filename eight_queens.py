
class Queen:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Board:

    def __init__(self, pos):
        self.queens = []
        for i in range(8):
            self.queens.append(Queen(i, pos[i]))  # one queen - one column

    def __is_queen(self, x, y):
        for queen in self.queens:
            if queen.x == x and queen.y == y:
                return True
        return False

    def set_pos(self, pos):
        for i in range(8):
            self.queens[i].y = pos[i]

    def is_done(self):
        for queen in self.queens:

            # horizontal
            for x in range(8):
                if x != queen.x and self.queens[x].y == queen.y:
                    return False

            # diagonal (lower-left -> upper-right)
            minc = min(queen.x, queen.y)
            x = queen.x - minc
            y = queen.y - minc
            while x < 8 and y < 8:
                if queen.x == x:
                    x += 1
                    y += 1
                    continue
                if self.queens[x].y == queen.y:
                    return False
                x += 1
                y += 1

            # diagonal (upper-left -> lower-right)
            minc = min(queen.x, 8 - queen.y)
            x = queen.x - minc
            y = queen.y + minc
            while x < 8 and y >= 0:
                if queen.x == x:
                    x += 1
                    y -= 1
                    continue
                if self.queens[x].y == queen.y:
                    return False
                x += 1
                y -= 1

        return True
