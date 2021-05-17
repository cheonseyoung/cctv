from socket import SOCK_STREAM, AF_INET, socket
from flask import Flask, render_template, request
import json
import protocol

## client
while True:
    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    got_data = protocol.receive_data(clientSocket)

    print(got_data)