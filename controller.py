from view import View

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

#must be at the end in order to circular importing work correctly (from controller import take_number_from_user)
from model import Board