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

    @staticmethod
    def take_number_from_user():
        while True:
            try:
                number = int(input("From 1 to 100: "))
            except ValueError:
                print("Sorry, I didn't understand that.")
            if 0 < number < 101:
                break
            else:
                continue
        return number

    def start_higher_lower(self):
        message = self.s.recv(10240).decode()
        print(message)
        number = self.take_number_from_user()
        self.s.send(str(number).encode())
        while True:
            message = self.s.recv(10240).decode()
            if message == "equal":
                print("You won")
                return
            elif message == "lower":
                print("lower")
            elif message == "higher":
                print("higher")
            number = self.take_number_from_user()
            self.s.send(str(number).encode())


if __name__ == '__main__':
    client = Client()
    print("Which game you choose? \n0-tic tac toe \n1- higher/lower")
    while True:
        try:
            number = int(input("0 or 1?: "))
        except ValueError:
            print("Sorry, I didn't understand that.")
        if 0 <= number < 2:
            break
        else:
            continue
    if number == 0:
        client.start_tic_tac_toe()
    else:
        client.start_higher_lower()

