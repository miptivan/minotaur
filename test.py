import socket
from _thread import *


# CLIENT
def connection(Server, Port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((Server, Port))
# / CLIENT


# SERVER
def cycle(s):
    while True:
        conn, addr = s.accept()  # Программа виснет, пока не подключется новый пользователь
        print("Connected to:", addr)
        res = conn.recv(1024)  # Принимаем пакет
        print(res)



def create_server(server, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаётся сокет

    try:
        s.bind((server, port))  # Назначаем ip для этого сокета
    except socket.error as e:
        str(e)

    s.listen()  # Переводим сокет в режим прослушки
    print("Waiting for a connection, Server Started")
    start_new_thread(cycle, (s,))  # Создаём один поток, в котором ловим все приходящие сокеты. Крч подключение
# / SERVER
