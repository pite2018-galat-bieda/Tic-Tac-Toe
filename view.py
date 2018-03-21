from abc import ABC
from abc import abstractmethod
import os
import platform


class ViewInterface(ABC):
    @abstractmethod
    def print_board(self):
        pass


class View(ViewInterface):
    user_symbol = [' ', 'X', 'O']

    @staticmethod
    def clear_screen():
        if(platform.system() == 'Linux'):
            os.system('clear')
        elif(platform.system() == 'Windows'):
            os.system('cls')
        else:
            print("Can not clear screen")

    def print_board(self, board):
        data = board.get_board()
        View.clear_screen()
        for a in data:
            print("| {} | {} | {} |\n".format(self.user_symbol[a[0]],
                                              self.user_symbol[a[1]],
                                              self.user_symbol[a[2]]))

