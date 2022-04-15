# Name: Dylan Mitchel Karambut
# Project: 1 - Sockets and HTTP
# Due Date: April 17, 2022
# Date Modified: April 15, 2022
# Description: The world’s simplest HTTP server

# Code Adapted From: https://pythontic.com/modules/socket/send

import socket
import random

random.seed()

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind + Listen Data
serverSocket.bind(("127.0.0.1", 8001))
serverSocket.listen()
print("Socket Listening at 8081!")

clientConnection, clientAddress = serverSocket.accept()
print("Connection: " + clientAddress[0] + ' ,' + str(clientAddress[1]))

text = clientConnection.recv(4096)
decode = text.decode("utf-8")
print(decode)

# Receive (Server -> Client)
data3 = "HTTP/1.1 200 OK\r\n"\
    "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
    "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

clientConnection.sendall(data3.encode("utf-8"))
print("")

clientConnection.close()
serverSocket.close()

# Run it by: python3 http-server.py