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
        self.about_users[addr]['conn'].send(str.encode('i'))
        volume = self.about_users[addr]['conn'].recv(10)
        info = self.about_users[addr]['conn'].recv(int(str(volume)))
        info = str(info)  # {'a': b}
        info = info[1:-1]
        print(info)
        # for param in info.split(', '):


class client():
    def __init__(self):
        self.info = None
        self.s = None
        self.info = None
        self.all_info = None
        self.info_volume = None
        self.state = None

    def set_info(self, info):
        self.info = info
        self.info_volume = len(str.encode(str(self.info)))

    def connect(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
        self.state = 1
        start_new_thread(self.caching_type_message())

    # waiting state
    # 1 is waiting mode
    def caching_type_message(self):
        while self.state == 1:
            type_msg = str.decode(self.s.recv(10))
            if type_msg == 'i':
                self.s.send(str.encode(str(self.info_volume)))
                self.s.send(str.encode(str(self.info)))

    def sender(self):
        self.state = int(str.decode(self.s.recv(5)))
        self.s.send(self.info_volume)
        while self.state == 1:
            volume = self.s.recv()
            self.s.send(str.encode('0'))
            # перейти в цикл принятия сообщения конкретного типа
