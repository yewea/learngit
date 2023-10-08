from socket import *


IP = '0.0.0.0'
PORT = 50000
BUFLEN = 512
listenSocket = socket(AF_INET, SOCK_STREAM)
listenSocket.bind((IP, PORT))
listenSocket.listen(5)
dataSocket, addr = listenSocket.accept()
