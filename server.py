import select
import socket
import pickle
import random
from model import Board

host = '127.0.0.1' 
port = 5005 
backlog = 5 
maxsize = 1024 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(backlog)
input = [server,]

var = 1
print("Serwer started")
print("Waiting for players")

new_game = Board()

for x in range(2):
    inputready,outputready,exceptready = select.select(input,[],[])
    print("Waiting for second player")

    for s in inputready: 
        if s == server: 
            client, address = server.accept()
            input.append(client) 
            print ( 'new client added%s'%str(address))
            if(var == 2):
                input[1].send(str.encode("oponent found"))
                input[2].send(str.encode("oponent found"))
            var += 1



# send empty board
data_string = pickle.dumps(new_game)
input[1].send(data_string)
input[2].send(data_string)
input[1].send(data_string)
while True:
    print("jestem w tej glownej petli")
    var += 1
    print(var%2+1)
    s=input[var%2+1]

  
    while True:
        # waiting for receive move
        data = s.recv(10240)
        lista = pickle.loads(data)
      
        # try to make move   
        if new_game.make_move(var%2+1,lista[1],lista[0]):
            if(new_game.check_win(var%2+1)):
                s.send(str.encode("won"))
            elif(new_game.check_draw()):
                s.send(str.encode("draw"))
            else:
                s.send(str.encode("pass"))
            data_string = pickle.dumps(new_game)
            break
        else:
            s.send(str.encode("This field is already occupied"))

    #actualize both boards
    input[1].send(data_string)
    input[2].send(data_string)

