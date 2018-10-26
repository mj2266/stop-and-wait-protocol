import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8000
print (host)
print (port)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            r=input("send data")
            clientsocket.send(r.encode())
            print(clientsocket.recv(1024).decode())
            """print('Client sent:', self.sock.recv(1024).decode())
            r=input("reply")
            self.sock.send(r.encode())"""

serversocket.listen(5)
print ('server started and listening')
while (True):
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
