import random


class Board:
    x, o, n = 'x', 'o', ' '
    moves = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2)
    }

    def __init__(self):
        self.last_move = ''
        self.board = [[' '] * 3 for _ in range(3)]

    def __str__(self):
        x = ''
        for i in self.board:
            for j in i:
                if j == ' ':
                    x += '🔳'
                elif j == 'o':
                    x += random.choice(['😀', '🙄', '🥱'])
                elif j == 'x':
                    x += random.choice(['😈', '👿'])
            x += '\n'
        return x[:-1]

    def is_winner(self):
        # lines
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != self.n or \
                    self.board[0][i] == self.board[1][i] == self.board[2][i] != self.n:
                return self.board[i][0]
        # diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != self.n or \
                self.board[0][2] == self.board[1][1] == self.board[2][0] != self.n:
            return self.board[1][1]
        # if draw
        if self.free_cells():
            return False
        return "tie"

    def free_cells(self):
        """Ckeck if there are some free cells"""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == self.n:
                    return True
        return False

    def make_move(self, move, player):
        """
        :param move: = number from input keyboard
        :param player: human or ai --> x or o
        """
        if move in self.moves:
            i, j = self.moves[str(move)][0], self.moves[str(move)][1]

            if self.board[i][j] == self.n:
                self.board[i][j] = player
                return True
        return False

    def all_moves(self):
        """Return all possible moves"""
        res = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == self.n:
                    res.append(str(3 * i + 1 + j))
                    # res.append(self.board[i][j])
        if len(res) > 0:
            return res
        return False

    def copy(self):
        """Mske a copy of current board without changing it"""
        new_b = Board()
        for i in range(3):
            for j in range(3):
                new_b.board[i][j] = str(self.board[i][j])
        return new_b


if __name__ == '__main__':
    board = Board()
    print(board[1][2])
