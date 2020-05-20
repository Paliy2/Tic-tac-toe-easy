from board import Board
from btree import BTree


class Game:
    """Class to initialize and perform Tic Tac Toe game"""

    def __init__(self):
        """ Init some parameters"""
        self.board = Board()
        self.move = 0
        self.player = 'x'
        self.ai = 'o'

    def print_board(self):
        """Output the current state of the game"""
        print()
        print(self.board)

    def get_move(self):
        """Get user move"""
        move = input('Your move: ').strip()
        while move not in Board.moves or move not in self.board.all_moves():
            print('Wrong input, try again')
            move = input('Please, enter 1-9 move(cells from top to down): ').strip()
        self.move = str(int(move))
        self.board.make_move(self.move, self.player)

    def ai_move(self):
        """Perform auto move"""
        tictak = BTree(self.board)
        new_move = tictak.make_tree(self.player, self.ai)[1]
        print('AI move:', new_move)
        self.board.make_move(new_move, self.ai)

    def get_player(self):
        """Make possibility to choose light/dark side;)"""
        player = input('Choose x/o: ').strip().lower()
        if player == 'o':
            self.player, self.ai = self.ai, self.player

    def get_winner(self):
        """Check if game is over"""
        win = self.board.is_winner()
        if win == self.player:
            return 'You have won'
        elif win == self.ai:
            return 'You are loser'
        elif win == 'tie':
            return 'Draw'


if __name__ == '__main__':
    session = Game()
    session.get_player()
    while not session.get_winner():
        if session.player == 'o':
            session.ai_move()
            session.print_board()
            if session.get_winner():
                break
            session.get_move()
        else:
            session.print_board()
            session.get_move()
            if session.get_winner():
                break
            session.ai_move()

    session.print_board()
    print(session.get_winner())

# scores = {
#     'x': 1,
#     'o': -1,
#     'tie': 0
# }
#
# ai = 'x'
# human = 'o'
# currentPlayer = human
#
# def minimax(board, depth, isMaximizing=False):
#     result = check_winner()
#     if result:
#         return scores[result]
#     if isMaximizing:
#         bestScore = -10
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == ' ':
#                     board[i][j] = ai
#                     score = minimax(board, depth + 1, False)
#                     board[i][j] = ' '
#                     bestScore = max(bestScore, score)
#         return bestScore
#     else:
#         bestScore = 10
#         for i in range(3):
#             for j in range(3):
#                 if board[i][j] == ' ':
#                     board[i][j] = human
#                     score = minimax(board, depth + 1, True)
#                     board[i][j] = ' '
#                     bestScore = min(score, bestScore)
#         return bestScore
