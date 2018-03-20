

class Board:
    def __init__(self):
        self.board = [[0]*3, [0]*3, [0]*3]

    def make_move(self, player, row, col):
        if (col < 3) & (row < 3) & (col >= 0) & (row >= 0):
            if self.board[row][col] == 0:
                self.board[row][col] = player
                return True
        return False

    def get_board(self):
        return self.board
