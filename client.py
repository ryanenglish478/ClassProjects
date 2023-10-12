import socket 

s = socket.socket()

port=12345

#connect to server on local pc
print('Connecting to server')
s.connect(('127.0.0.1', port))
print("Connected, to quit type 'quit'")
message = input(" -> ")
while message.lower().strip() != 'quit':
    s.send(message.encode())
    data = s.recv(1024).decode()

    print('Received from server: ' + data)

    message = input(" -> ")

s.close()
