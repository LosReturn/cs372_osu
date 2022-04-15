# Name: Dylan Mitchel Karambut
# Project: 1 - Sockets and HTTP
# Due Date: April 17, 2022
# Date Modified: April 15, 2022
# Description: Using a socket to GET a file & GET the data for a large file

# Code Adapted From: https://docs.python.org/3.8/howto/sockets.html

import socket
import random

## --- Using a socket to GET a file ---

# Create Socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect Server with Random Port
random.seed()
port = random.randint(1024, 9000)

clientSocket.connect(("gaia.cs.umass.edu", 80))

data = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

clientSocket.sendall(data.encode())

# Print Data (Client -> Server)
print("Request: ", data)

# Receive (Server -> Client)
data = clientSocket.recv(4096)
decode = data.decode()
print(decode)

## --- GET the data for a large file ---

data2 = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
clientSocket.sendall(data2.encode())

# Print Data (Client -> Server)
print("Request: ", data2)

# Receive (Server -> Client)
while 1:
    data2 = clientSocket.recv(4096)
    decode = data2.decode()
    print(decode)

    # Length decoded = 0, no more data
    if len(decode) == 0:
        print("No More Data!")
        break

clientSocket.close()

# Run it by: python3 connect_socket.py