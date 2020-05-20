class BTNode:
    """Node for tic tac toe game"""

    def __init__(self, board=None):
        self.board = board
        self.left = None
        self.right = None

    def __str__(self):
        res = ''
        for i in self.board:
            for j in i:
                if j != ' ':
                    res += j + ' '
                else:
                    res += '🔳'
            res += '\n'
        return res
