from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread


class Server(object):
    def __init__(self):
        self.PORT = 33000
        self.BUFSIZ = 1024
        self.ADDR = ("", self.PORT)
        self.SERVER = socket(AF_INET, SOCK_STREAM)
        self.SERVER.bind(self.ADDR)

    def accept_connection(self):
        while True:
            client, client_address = self.SERVER.accept()



class Client(object):#will be moved to client project
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 33000
        self.BUFSIZ = 1024
        self.ADDR = (self.HOST, self.PORT)
        self.SERVER = socket(AF_INET, SOCK_STREAM)
        self.SERVER.bind(self.ADDR)

    def send_object(self, obj):
        



