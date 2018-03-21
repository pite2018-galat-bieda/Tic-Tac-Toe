from view import View
from model import Board
	
def start():
    new_game = Board()
    view = View()

    while True:    
	    for player_number in range(1,3):
	    	view.print_board(new_game)
	    	new_game.make_move(player_number)
	    	if(new_game.check_win(player_number)):
	    		print("Congratulations! Player " + str(player_number) + " won!")
	    		return
	    	if(new_game.check_draw()):
	    		print("Draw!")
	    		return

