import socket
import pickle
from model import Board
from view import View


class Client:
    def __init__(self):
        self.TCP_IP = '127.0.0.1'
        self.TCP_PORT = 5005
        self.BUFFER_SIZE = 1024

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.TCP_IP, self.TCP_PORT))

    def start_tic_tac_toe(self):
        print("Waiting for other players")
        view = View()
        while True:
            data = self.s.recv(10240)
            new_game = pickle.loads(data)
            view.print_board(new_game)

            print("waiting for opponent move")
            data = self.s.recv(10240)
            new_game = pickle.loads(data)
            view.print_board(new_game)
            while True:
                column_number = Board.take_number_from_user('column')
                row_number = Board.take_number_from_user('row')
                data_list = [column_number, row_number]
                print(data_list)
                data = pickle.dumps(data_list)
                self.s.send(data)
                message = self.s.recv(10240).decode()
                if message != "This field is already occupied":
                    if message == "draw":
                        print("Draw")
                        return
                    elif message == "won":
                        print("You won")
                        return
                    else:
                        break
                else:
                    print("This field is already occupied")


if __name__ == '__main__':
    client = Client()
    client.start_tic_tac_toe()
