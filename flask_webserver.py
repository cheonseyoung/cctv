from socket import SOCK_STREAM, AF_INET, socket
from flask import Flask, render_template, request
import json
import protocol


app = Flask(__name__)

@app.route('/')
def test():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def cal():

    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        dict_data = {'aa' : a, 'bb' : b }

    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    protocol.send_data(clientSocket , data=dict_data)
    got_data = protocol.receive_data(clientSocket)

    return render_template('info.html', got_data=got_data)


@app.route('/show')
def show():
    return render_template('show_words.html')




if __name__ == '__main__':
    app.run()

