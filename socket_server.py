from multiprocessing import Process, Lock, Manager
import protocol
import socket

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

    dataset = []
    while True:
        try:
            client, address = server_socket.accept()

            # receive request
            request_data = protocol.flask_webserver(client)
            dataset += [request_data]

            # send response
            response_data = sum(dataset)
            protocol.send_data(client, response_data)

            client.close()
        except Exception as e:
            break

    server_socket.close()

if __name__ == '__main__':
    server_start()



