import socket
from _thread import *
import sys


hostname = socket.gethostname()
server = socket.gethostbyname(hostname)
port = 5555


def get_ip():
    global server
    global port
    return f'{server}:{port}'


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()


def cycle(s):
    while True:
        conn, addr = s.accept()
        print("Connected to:", addr)
        res = conn.recv(1024)
        print(res)

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
    #s.close()

def connection(Server, Port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((Server, Port))
    s.send(b'hello)')
    #s.close()