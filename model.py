
class Board:
    def __init__(self):
        self.board = [[0]*3, [0]*3, [0]*3]

    @staticmethod
    def take_number_from_user(col_or_row):
        while True:
            try:
                number = int(input("Give " + col_or_row + " number from 0 to 2: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
            if(0 <= number <= 2):
                break
            else:
                continue
        return number

    def try_make_move(self, player, row, col):
        if (col < 3) & (row < 3) & (col >= 0) & (row >= 0):
            if self.board[row][col] == 0:
                self.board[row][col] = player
                return True
        return False

    def get_board(self):
        return self.board

    def make_move(self, player_number):
        print("Player " + str(player_number) + " turn")
        while True:
            row_number = self.take_number_from_user("row")
            column_number = self.take_number_from_user("column")
            if(self.try_make_move(player_number, row_number, column_number)):
                break
            else:
                print("This field is already occupied")
    
    def check_win(self, player):
        return (
            (self.board[0][0]==player and self.board[0][1] == player and self.board[0][2] == player) or
            (self.board[1][0]==player and self.board[1][1] == player and self.board[1][2] == player) or
            (self.board[2][0]==player and self.board[2][1] == player and self.board[2][2] == player) or

            (self.board[0][0]==player and self.board[1][0] == player and self.board[2][0] == player) or
            (self.board[0][1]==player and self.board[1][1] == player and self.board[2][1] == player) or
            (self.board[0][2]==player and self.board[1][2] == player and self.board[2][2] == player) or

            (self.board[0][0]==player and self.board[1][1] == player and self.board[2][2] == player) or
            (self.board[0][2]==player and self.board[1][1] == player and self.board[2][0] == player))

    def check_draw(self):
        flat_board = [item for row in self.board for item in row]
        return False if 0 in flat_board else True
