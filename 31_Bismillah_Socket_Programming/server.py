import socket

ss = socket.socket()

print("Server Socket Created ")

ss.bind(('localhost', 9999))


ss.listen(3)
print("Waiting for connections")

while True:
    
    cs, addr = ss.accept()
    cs2, addr2 = ss.accept()

    name = cs.recv(1024).decode()
    name2 = cs2.recv(1024).decode()

    print("Connected with Client ", addr, name)
    print("Connected with Client ", addr2, name2)

    #cs.send(bytes("Welcome to Tiger's Dent", "utf-8"))
    
    cs.send(bytes("Welcome to Tiger's Dent", "utf-8"))
    cs2.send(bytes("Welcome to Royal's Dent", "utf-8"))

    print("Let's Start Chatting.......... ")

    while True:
        msg1 = cs.recv(1024).decode()
        msg2 = cs2.recv(1024).decode()

        cs.send(bytes(msg2, "utf-8"))
        cs2.send(bytes(msg1, "utf-8"))

    cs.close()
    cs2.close()






