import socket
from _thread import *
from matze import matze


hostname = socket.gethostname()
server = socket.gethostbyname(hostname)
port = 5555
STATE_GAME = 0  # 0 - Ожидание, 1 - Игра началась


def get_ip():
    global server
    global port
    return f'{server}:{port}'


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        if STATE_GAME == 1:
            labirint = matze(25, 25)
            labirint.dfs()
            conn.send(bytes(str(labirint.space)))


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


def connection(Server, Port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((Server, Port))
    while True:
        labirint = s.recv(50*50*8*3)
        print(labirint)
