import socket
from _thread import *

class server():
    def __init__(self, port=5555):
        self.about_users = {}  # {id: {}}
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = port
        self.s = None  # socket сервера
        self.STATE_SERVER = None
    
    def get_ip(self):
        return (self.ip, self.port)

    def cacther_cycle(self, s):
        while self.STATE_SERVER == 1:
            conn, addr = s.accept()
            self.about_users[addr] = {'conn': conn}
        
    def catcher(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.bind((Server, Port))
        except socket.error as e:
            str(e)
        self.STATE_SERVER = 1 # - состояние ловли клиентов
        start_new_thread(self.cacther_cycle, (s,))
    
    def get_info(self, addr):
        self.about_users[addr]['conn'].send(str.encode('info'))
        volume = self.about_users[addr]['conn'].recv(10)
        info = self.about_users[addr]['conn'].recv(int(str(volume)))
        info = str(info)  # {'a': b}
        info = info[1:-1]
        print(info)
        #for param in info.split(', '):


class client():
    def __init__(self):
        self.info = None
        self.s = None
        self.info = None
        self.all_info = None
        self.info_volume = None
    
    def connect(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
    
    def waiter(self):
        while self.state = 1:
            s

    def sender(self):
        self.state = int(str.decode(self.s.recv(5)))
        self.s.send(self.info_volume)
        while self.state == 1:
            volume = self.s.recv()
