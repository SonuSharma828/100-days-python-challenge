import socket

# Create a socket object
s = socket.socket()
print('Socket created')

# Bind the socket to localhost on port 5868
s.bind(('localhost', 5868))

# Listen for incoming connections, with a queue of up to 3
s.listen(3)
print('Waiting for connection')

# Infinite loop to accept multiple connections
while True:
    # Accept a connection and get the client socket and address
    c, addr = s.accept()
    
    # Receive the client's name
    name = c.recv(1024).decode()
    
    # Print connection details and client name
    print('Connected with', addr, name)
    
    # Send a welcome message to the client
    c.send(bytes('Welcome to the server', 'utf-8'))
    
    # Close the client connection
    c.close()
  
