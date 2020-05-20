from btnode import BTNode
import random


class BTree:
    """Tree for auto moves in game Tic Tac Toe"""

    def __init__(self, board=None):
        self.root = BTNode(board)

    def make_tree(self, player, ai):
        """
        :param player: x or o sign
        :param ai: o or x sign
            light/dark side
        """

        def get_move(root, depth):
            """
            :param root: head node of Board Binary Tree
            :param depth: number of recursion iterations to check player
            """
            if not root:
                return -1000, None
            winner = root.board.is_winner()
            if winner == player:
                return 1, None
            elif winner == ai:
                return -1, None
            elif winner == 'tie':
                return 0, None
            if depth % 2 == 0:
                current = player
            else:
                current = ai

            all_moves = root.board.all_moves()
            right = ()
            left = ()

            if all_moves:
                right = random.choice(all_moves)
                all_moves.remove(right)
                new_b = root.board.copy()
                new_b.make_move(right, current)
                root.right = BTNode(new_b)

            if all_moves:
                left = random.choice(all_moves)
                all_moves.remove(left)
                new_b = root.board.copy()
                new_b.make_move(left, current)
                root.left = BTNode(new_b)
            # print('Board: ', new_board)
            right_data = get_move(root.right, depth + 1)[0]
            left_data = get_move(root.left, depth + 1)[0]

            if right_data > left_data:
                return right_data + left_data, right
            return right_data + left_data, left

        return get_move(self.root, 0)
