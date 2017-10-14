from socket import socket

sock = socket()
sock.connect(("localhost", 9090))
sock.send("hello".encode("utf-8"))

data = sock.recv(1024)
sock.close()

print(data.decode("utf-8"))
input()