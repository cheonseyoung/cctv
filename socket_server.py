
from multiprocessing import Process, Lock, Manager
import protocol
import socket
import json
import datetime
from threading import Thread
import time

def server_start():

    server_socket = socket.socket()
    host = ''
    port = 12000
    try:
        server_socket.bind((host, port))
    except socket.error as e:
        server_socket.close()
        return
    server_socket.listen()

    while True:
        try:
            time.sleep(1)
            client, address = server_socket.accept()
            # send request
            data = str(datetime.datetime.now())
            print(data)
            protocol.send_data(client, data=data)
            client.close()
        except Exception as e:
            break

    server_socket.close()

if __name__ == '__main__':
    while True:
        server_start()
