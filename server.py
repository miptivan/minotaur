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