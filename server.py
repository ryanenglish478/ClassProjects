import socket

s = socket.socket()
print("Socket successfully created")
#Reserve port on computer
port = 12345

#bind port to socket without ip address
#So server listens to requests
s.bind(('', port))

#put socket into listening mode
s.listen(5)
print("socket is listening")

while True:
    #establish connection with client
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connectiong'.encode())
    c.close()
    break
