import socket

# Create a client socket object
c = socket.socket()

# Connect the client to the server on localhost and port 5868
c.connect(('localhost', 5868))

# Prompt the user for their name and send it to the server
name = input("Enter your name: ")
c.send(bytes(name, 'utf-8'))

# Receive and print the server's welcome message
print(c.recv(1024).decode())
