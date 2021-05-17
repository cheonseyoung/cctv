from socket import SOCK_STREAM, AF_INET, socket
from flask import Flask, render_template, request
import json
import protocol
import datetime

app = Flask(__name__)

n = int(input())



## text파일에 저장된 file_path, url 정보를 value 함수를 이용 읽어오기 (마지막에 새롭게 업데이트 된 값들 중 마지막 값)
def value():
    f = open("C:/Users/테스터/Desktop/save.txt", 'r')
    try:
        line = f.readlines()
        line = line[-1].split(',')

    except:
        line = ['', '', '']
    return [line[1], line[2][:-1]]

##submit버튼을 누를시 각 칸에 입력된 값들을 set_value 리스트 저장하고, 이를 화면에 다시에 보여주기 위한 작업.
@app.route('/submit_button', methods=['POST'])
def methodd(num_list=[]):
    new_file_path = ''
    new_url = ''

    arr=[[0,0]]
    get_value = value()
    if request.method == 'POST':
        for i in range(1,n+1):
            file_path = request.form['File_Path'+str(i)]
            url = request.form['Url'+str(i)]
            arr+=[[file_path,url]]


            if file_path!= new_file_path and file_path != get_value[0]:
                new_file_path = file_path
            if url!= new_url and url != get_value[1]:
                new_url= url

        ## txt 파일에 업데이트 내용 저장
        with open("C:/Users/테스터/Desktop/save.txt", "a", encoding='utf-8') as f:
            f.write("\n")
            f.write("< %s >\n" % (datetime.datetime.now()))
            for i in range(n):
                f.write("%d th,%s,%s\n" % (i, arr[i][0], arr[i][1]))
            f.write("%s,%s,%s\n" % ('update_file_info', new_file_path, new_url))


    return render_template('cctv_submit.html',num=n,arr=arr)

#
@app.route('/')
def test(numlist=[]):
    arr=value()
    return render_template('cctv.html', num=n,arr=arr)

if __name__ == '__main__':
    app.run()