import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 16001))
s.listen(1)
client, client_address = s.accept()
print(client)
s.send(b"Connection received!")
