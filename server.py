import socket
import sys

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
#establish connection with client
conn, addr = s.accept()
print('Got connection from', addr)

while True:
  data = conn.recv(1024).decode()
  if not data:
    break
  print('Received from client: ' + data)

  message = input(" -> ")
  conn.send(message.encode())




conn.close()

