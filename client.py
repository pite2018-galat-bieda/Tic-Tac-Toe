import socket
import socket
import pickle
from model import Board
from view import View

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

def start():
    print("Waiting for other players")
    message = s.recv(10240)
    print(message.decode())

    view = View()

    while True:
        data = s.recv(10240)
        new_game = pickle.loads(data)
        view.print_board(new_game)

        print("waiting for oponent move")
        data = s.recv(10240)
        new_game = pickle.loads(data)
        view.print_board(new_game)
        while True:
            
            column_number = Board.take_number_from_user('column')
            row_number = Board.take_number_from_user('row')
            lista = [column_number, row_number]
            print(lista)
            data=pickle.dumps(lista)
            s.send(data)
            message = s.recv(10240).decode()
            if (message != "This field is already occupied"):
                if (message == "draw"):
                    print("Draw")
                    return
                elif (message == "won"):
                    print("You won")
                    return
                else:
                    break
            else:
                print("This field is already occupied")

start()