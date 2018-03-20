from view import View
from model import Board


def start():
    new_game = Board()
    view = View()
    view.print_board(new_game)


