import socket

cs = socket.socket()

cs.connect(('localhost', 9999))
name = input("Enter your Name: ")
cs.send(bytes(name, 'utf-8'))

print(cs.recv(1024).decode())

while True:
    msg1 = input("Enter a Message: ")
    cs.send(bytes(msg1, 'UTF-8'))
    print(cs.recv(1024).decode())



