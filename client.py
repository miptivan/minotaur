import socket
from _thread import *
from matze import matze
import numpy as np

labirint = None

STATE_GAME = 0  # 0 - Ожидание, 1 - готовность к игре

def client(Server, Port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((Server, Port))# connetcting to the server
    start_new_thread(cycle_client, (s,))

def cycle_client(s):
    global labirint
    labirint = s.recv(50*50*8*3)
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
    s.send(str.encode('1'))
    STATE_GAME = 1 # 1 - готовность к игре
    STATE_GAME = int(str.decode(s.recv(5)))
    if STATE_GAME == 2:
        s.send(str.encode('2'))
