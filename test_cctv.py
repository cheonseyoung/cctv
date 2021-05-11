from socket import SOCK_STREAM, AF_INET, socket
from flask import Flask, render_template, request
from flask_socketio import SocketIO
import json
import protocol
import datetime

app = Flask(__name__)
socketio=SocketIO

n = int(input())

##submit버튼을 누를시 각 칸에 입력된 값들을 set_value 리스트 저장하고, 이를 화면에 다시에 보여주기 위한 작업.
@app.route('/methodd', methods=['POST'])
def methodd(num_list=[]):
    return render_template('cctv_submit',data='aaa')

def value():
    f = open("C:/Users/테스터/Desktop/save.txt", 'r')
    try:
        line = f.readlines()
        line = line[-1].split(',')

    except:
        line = ['', '', '']
    return [line[1], line[2][:-1]]

#
@app.route('/')
def test(numlist=[]):
    get_value = value()
    return render_template('cctv.html', num_list=n, get_value1=str(get_value[0]), get_value2=str(get_value[1]))

