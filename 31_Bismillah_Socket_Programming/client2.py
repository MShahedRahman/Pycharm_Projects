import socket

cs2 = socket.socket()

cs2.connect(('localhost', 9999))
name2 = input("Enter your Name: ")
cs2.send(bytes(name2, 'utf-8'))

print(cs2.recv(1024).decode())

while True:
    msg2 = input("Enter a Message: ")
    cs2.send(bytes(msg2, 'UTF-8'))
    print(cs2.recv(1024).decode())




