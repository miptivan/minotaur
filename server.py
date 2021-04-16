import socket
from _thread import *
from matze import matze

labirint = None

hostname = socket.gethostname()
server = socket.gethostbyname(hostname)
port = 5555
STATE_GAME = 0  # 0 - Ожидание, 1 - Игра началась


def get_ip():
    global server
    global port
    return f'{server}:{port}'


def threaded_client(conn):
    global labirint
    while True:  # ждём начала игры
        if STATE_GAME == 1:
            labirint = matze(25, 25)
            labirint.dfs()
            labirint = labirint.space
            conn.send(str.encode(str(labirint)))
            while True:
                pass  # цикл игры


def cycle(s):
    while STATE_GAME == 0:
        conn, addr = s.accept()
        print("Connected to:", addr)
        start_new_thread(threaded_client, (conn,))


def create_server(server, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)
    s.listen()
    print("Waiting for a connection, Server Started")
    start_new_thread(cycle, (s,))
    # s.close()


def cycle_client(s):
    global labirint
    labirint = s.recv(50*50*8*3)
    print(labirint)
    labirint = str.decode(labirint)
    labirint = labirint[1:-1]
    res = []
    i = 0
    for s in labirint.split('\n'):
        res.append([])
        s = s[1:-1]
        for m in s.split(' '):
            res[i].append(float(m))
        i += 1
    labirint = np.array(res)
    while True:  # Цикл игры
        pass


def connection(Server, Port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((Server, Port))
    start_new_thread(cycle_client, (s,))


import socket
from _thread import *
from matze import matze

labirint = None

hostname = socket.gethostname()
Server = socket.gethostbyname(hostname)
Port = 5555
STATE_GAME = 0  # 0 - Ожидание, 1 - Игра началась


def state_machine():
    def __init__(self):
        self.clients_state = {}
        self.n = 0
    
    def check_states(i):
        res = 0
        for j in self.clients_state:
            if self.clients_state[j] == i:
                res += 1
        if res == self.n:
            return True
        else:
            return False
    
    def add(x):
        self.clients_state[self.n] = x
        self.n += 1

clients_state = state_machine()


def get_ip():
    global Server
    global Port
    return f'{Server}:{Port}'

def server():
    global Server
    global Port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((Server, Port))
    except socket.error as e:
        str(e)
    s.listen()
    print("Waiting for a connection, Server Started")
    labirint = matze(25, 25)
    labirint.dfs()
    labirint = labirint.space
    print('labirint is created')
    start_new_thread(answer_cycle, (s,))

def answer_cycle(s):
    global clients_state
    global STATE_GAME
    while STATE_GAME == 0:
        conn, addr = s.accept()
        conn.send('connected')
        print("Connected to:", addr)
        start_new_thread(threaded_client, (conn,))
    # change State_game
    
    while not clients_state.check_states(2):
        pass

    STATE_GAME = 2

    while STATE_GAME != 0:
        conn, addr = s.accept()
        conn.send('too late')


def threaded_client(conn):
    global labirint
    global clients_state
    local_number = clients_state.add(0) # 0 - ждет начала игры
    while True:  # ждём начала игры
        if STATE_GAME == 1: # 1 - готовность
            conn.send(str.encode(str(labirint)))
            clients_state.clients_state[local_number] = int(str.decode(conn.recv(5)))
            while not clients_state.check_states(1):
                pass # ждем пока все получать лабиринт
            conn.send(str.encode('2'))
            clients_state.clients_state[local_number] = int(str.decode(conn.recv(5)))
            if clients_state.check_states(2):
                print('yeah, all get lab!!')
            
            