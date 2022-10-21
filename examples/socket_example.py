import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 16001))
s.send(b'Hello world!')

s.recv(1000)

