# Python Socket Chat Application

This project demonstrates a simple server-client communication using Python sockets. It includes two main files:
- `SocketMain.py`: The server-side code.
- `SocketClient.py`: The client-side code.

## Setup
To run this application, you need Python 3 installed on your machine.

## Instructions

1. **Run the Server**  
   Start the server by executing `SocketMain.py`.
   ```bash
   python SocketMain.py
2.Run the Client
Open a new terminal and run 
   ```bash
    python SocketClient.py
3.Enter Your Name
The client will prompt you to enter your name. Type your name and press Enter to connect to the server.

4.Server Response
Once connected, the server will display a welcome message for the client, and the client will print the message received from the server

How It Works
* The server listens for connections on localhost and port 5868.
* The client connects to the server on the same port.
* After connecting, the client sends its name to the server, and the server responds with a welcome message

## This basic setup can be expanded for more complex multi-client chat applications


This setup should help you understand and use the server-client socket communication. Let me know if you need any further modifications!
