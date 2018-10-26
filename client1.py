import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="localhost"
port =8000
s.connect((host,port))

"""def ts(str):
   s.send(str.encode()) 
   data = ''
   data = s.recv(1024).decode()
   print (data)"""

while 2:
   data=s.recv(1024).decode()
   print(data+" received")
   str="acknowledgement received"
   s.send(str.encode())

s.close ()
