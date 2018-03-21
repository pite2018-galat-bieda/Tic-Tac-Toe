from view import View
from model import Board

def new_turn(view, board):
	for player_number in range(1,3):
		view.print_board(board)
		while True:
			print("Player " + str(player_number) + " turn")
			while True:
			    try:
			        row_number = int(input("Give row number from 0 to 2: "))
			    except ValueError:
			        print("Sorry, I didn't understand that.")
			        continue
			    if(row_number<0 or row_number>2):
			    	continue
			    else:
			        break
			while True:
			    try:
			        column_number = int(input("Give column number from 0 to 2: "))
			    except ValueError:
			        print("Sorry, I didn't understand that.")
			        continue
			    if(column_number<0 or column_number>2):
			    	continue
			    else:
			        break
			if(board.make_move(player_number,row_number, column_number)):
				break
			print("This field is already occupied")
		if(board.check_win(player_number)):
			view.print_board(board)
			print("Player " + str(player_number) + " won")
			return False
	return True
	
def start():
    new_game = Board()
    view = View()
    
    view.print_board(new_game)
    while new_turn(view, new_game):
    	pass
