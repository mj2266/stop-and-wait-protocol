import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8000

serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            r=input("Send data -->")
            clientsocket.send(r.encode())
            print(clientsocket.recv(1024).decode())
            

serversocket.listen(5)
print ('Sender ready and is listening')
while (True):

    #to accept all incoming connections
    clientsocket, address = serversocket.accept()
    print("Receiver "+str(address)+" connected")
    #create a different thread for every 
    #incoming connection 
    client(clientsocket, address)
