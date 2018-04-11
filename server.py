import socket
import pickle
from model import Board


class Server:
    def __init__(self):
        self.host = '127.0.0.1' 
        self.port = 5005 
        self.backlog = 5 

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(self.backlog)
        self.clients = []

        self.new_game = Board()
        self.current_client = 0

        print("Server started")

    def next_client(self):
        self.current_client += 1
        self.current_client %= 2
        return self.current_client

    def wait_for_players(self):
        for _ in range(2):
            client, address = self.server.accept()
            self.clients.append(client)
            print('new client added%s' % str(address))

    def start_tic_tac_toe(self):
        self.wait_for_players()
        data_string = pickle.dumps(self.new_game)
        self.clients[0].send(data_string)
        self.clients[1].send(data_string)
        self.clients[0].send(data_string)
        while True:
            print("I am in this loop")
            s = self.clients[self.current_client]
            self.next_client()

            while True:
                print("waiting")
                # waiting for receive move
                data = s.recv(10240)
                print("rec")
                data_list = pickle.loads(data)

                # try to make move
                if self.new_game.make_move(self.current_client + 1, data_list[0], data_list[1]):
                    if self.new_game.check_win(self.current_client + 1):
                        s.send(str.encode("won"))
                    elif self.new_game.check_draw():
                        s.send(str.encode("draw"))
                    else:
                        s.send(str.encode("pass"))
                    data_string = pickle.dumps(self.new_game)
                    break
                else:
                    s.send(str.encode("This field is already occupied"))

            # actualize both boards
            self.clients[0].send(data_string)
            self.clients[1].send(data_string)


if __name__ == '__main__':
    server = Server()
    server.start_tic_tac_toe()

